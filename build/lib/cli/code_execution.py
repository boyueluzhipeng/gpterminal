# Standard library
import os
from queue import Queue
from subprocess import PIPE, Popen
from threading import Thread

# Local
# from DXRExplain.utilities.parsers import get_code_exec_command, get_error_message

GRAY = "\033[37m"
END = "\033[0m"

# Standard library
import re


######
# MAIN
######


def get_language(args):
    """
    Returns the language a file is written in.
    """

    file_path = args[1].lower()
    if file_path.endswith(".py"):
        return "python"
    elif file_path.endswith(".js"):
        return "node"
    elif file_path.endswith(".go"):
        return "go run"
    elif file_path.endswith(".rb"):
        return "ruby"
    elif file_path.endswith(".java"):
        return "javac" # Compile Java Source File
    elif file_path.endswith(".class"):
        return "java" # Run Java Class File
    else:
        return "" # Unknown language


def get_code_exec_command(args, language):
    fp_and_args = args[1:]
    if language == "java":
        fp_and_args = [arg.replace(".class", "") for arg in fp_and_args]

    return [language] + fp_and_args


def get_error_message(error, language):
    """
    Filters the stack trace from stderr and returns only the error message.
    """

    if error == '' or error is None:
        return None
    elif language == "python":
        if any(e in error for e in ["KeyboardInterrupt", "SystemExit", "GeneratorExit"]): # Non-compiler errors
            return None
        else:
            return error
    elif language == "node":
        return error.split('\n')[4][1:]
    elif language == "go run":
        return error.split('\n')[1].split(": ", 1)[1][1:]
    elif language == "ruby":
        error_message = error.split('\n')[0]
        return error_message[error_message.rfind(": ") + 2:]
    elif language == "javac":
        m = re.search(r'.*error:(.*)', error.split('\n')[0])
        return m.group(1) if m else None
    elif language == "java":
        for line in error.split('\n'):
            # Multiple error formats
            m = re.search(r'.*(Exception|Error):(.*)', line)
            if m and m.group(2):
                return m.group(2)

            m = re.search(r'Exception in thread ".*" (.*)', line)
            if m and m.group(1):
                return m.group(1)

        return None


#########
# HELPERS
#########


def read(pipe, funcs):
    """
    Reads and pushes piped output to a shared queue and appropriate lists.
    """

    for line in iter(pipe.readline, b''):
        for func in funcs:
            func(line.decode("utf-8"))

    pipe.close()


def write(get):
    """
    Pulls output from shared queue and prints to terminal.
    """

    print()
    for line in iter(get, None):
        line = line.replace("\n", "")
        print(f"{GRAY}{line}{END}")


######
# MAIN
######


def execute_code(args, language):
    """
    Executes a given command in a subshell, pipes stdout/err to the current
    shell, and returns the stderr.
    """
    command = get_code_exec_command(args, language)
    print(" ".join(command))
    process = Popen(
        command,
        cwd=None,
        shell=False,
        close_fds=True,
        stdout=PIPE,
        stderr=PIPE,
        bufsize=-1
    )

    output, errors = [], []
    pipe_queue = Queue()

    # Threads for reading stdout and stderr pipes and pushing to a shared queue
    stdout_thread = Thread(target=read, args=(process.stdout, [pipe_queue.put, output.append]))
    stderr_thread = Thread(target=read, args=(process.stderr, [pipe_queue.put, errors.append]))

    # Thread for printing items in the queue
    writer_thread = Thread(target=write, args=(pipe_queue.get,))

    # Spawns each thread
    for thread in (stdout_thread, stderr_thread, writer_thread):
        thread.daemon = True
        thread.start()

    process.wait()

    for thread in (stdout_thread, stderr_thread):
        thread.join()

    pipe_queue.put(None)

    # output = ''.join(output)
    errors = '\n'.join(errors)
    
    # 合并错误信息
    # if len(errors) > 0:
    #     errors = output + '\n' + errors

    # File doesn't exist, for java, command[1] is a class name instead of a file
    if "java" != command[0] and not os.path.isfile(command[1]):
        return None

    return get_error_message(errors, language)


def construct_query(language, error_message):
    # TODO: Create an class for mapping languages to exec commands
    language = "java" if language == "javac" else language
    language = "python" if language == "python3" else language
    language = "go" if language == "go run" else language
    print()
    query = f"Explain this {language} error message in brief and simple terms:"
    query += "\n```"
    query += f"\n{error_message}"
    query += "\n``` 给出详细的中文解决方案，以及修改建议，如果涉及到环境配置，请给出详细的环境配置步骤。"
    print()
    return query

# Standard library
import sys
import re
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

# Third party
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter

CODE_IDENTIFIER = "```"
CODE_INDENT = "    "

# ASCII color codes
CYAN = "\033[36m"
RED = "\033[31m"
END = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

INLINE_BY_STAR_IDENTIFIER = "\*(.*?)\*"
INLINE_BY_DASH_IDENTIFIER = "`(.*?)`"


#########
# HELPERS
#########


def handle_inline_code(text):
    replacer = lambda s: f"{BOLD}{s.group()}{END}"
    text = re.sub(INLINE_BY_STAR_IDENTIFIER, replacer, text)
    text = re.sub(INLINE_BY_DASH_IDENTIFIER, replacer, text)

    return text


def slow_print(text, delay=0.01):
    for word in text:
        sys.stdout.write(word)
        sys.stdout.flush() # Defeat buffering

        sleep(delay)


def slow_print_code(text, delay=0.0025):
    code = highlight(
        text,
        lexer=get_lexer_by_name("python"),
        formatter=Terminal256Formatter(style="gruvbox-dark")
    )
    for line in code.strip().split("\n"):
        slow_print(f"{CODE_INDENT}{line}", delay)
        print()


######
# MAIN
######


def print_help_message():
    """
    Prints usage instructions.
    """

    print(f"{BOLD}DXRExplain – Made by @shobrook{END}")
    print("Command-line tool that automatically explains your error message using ChatGPT.")
    print(f"\n\n{UNDERLINE}Usage:{END} $ DXRExplain {CYAN}[file_name]{END}")
    print(f"\n$ python3 {CYAN}test.py{END}   =>   $ DXRExplain {CYAN}test.py{END}")


def print_invalid_language_message():
    print(f"\n{RED}Sorry, DXRExplain doesn't support this file type.\n{END}")


class LoadingMessage:
    def __init__(self, timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """

        # self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.steps = ['-', '/', '|', '\\']
        self.message = f"{BOLD}{CYAN}正在让ChatGPT帮你查看错误{END}"
        self.end = f"{BOLD}{CYAN}🤖 ChatGPT的解释是:{END}"
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns

        print(f"\r{' ' * cols}", end="", flush=True)
        print(f"\r{self.end}\n", flush=True)

    def _animate(self):
        for step in cycle(self.steps):
            if self.done:
                break

            print(f"\r{CYAN}{step}{END} {self.message}", flush=True, end="")

            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_value, tb):
        self.stop()


def print_error_explanation(explanation):
    for i in explanation:
        print(i, end="", flush=True)
    print()

