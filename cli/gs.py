import json
import subprocess
import click
import sys
import openai
from rich.live import Live
from rich.markdown import Markdown
from .code_execution import *
from .cli import get_api_key
from .command_print import *
from rich import print
from rich.text import Text
import random
import readline
# 配置 readline
readline.parse_and_bind("set enable-meta-key on")
readline.parse_and_bind("set input-meta on")
readline.parse_and_bind("set output-meta on")
readline.parse_and_bind("set convert-meta off")
sys.stdin.reconfigure(encoding='utf-8')


def print_colorful(content):
    text = Text()
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    for char in content:
        color = random.choice(colors)
        text.append(char, style=f"bold {color}")
    print(text, end="", flush=True)
    
def ask_user_execute():
    # 默认是执行的
    while True:
        user_input = input("是否执行命令? [Y/n]: ")
        # 如果直接回车, 默认是执行的
        if user_input.strip() == "":
            return True
        if user_input.strip().lower() == "n":
            return False
        elif user_input.strip().lower() == "y":
            return True
        else:
            print("请输入 Y 或 n")
  
def execute_command(command):
    subprocess.run(command, shell=True)          


# def gpterminal():
#     """Figlu command line tool"""
#     print("Welcome to GPTerminal!")
#     pass

@click.group(invoke_without_command=True)  # 添加 invoke_without_command 参数
@click.option("--model", default="gpt-3.5-turbo", help="Specify which GPT model to use")
@click.option("--maxtoken", default=4096, help="Maximum number of tokens in a single prompt")
def gpterminal(model, maxtoken):
    """Generate and execute command line code based on user input"""
    base_url, api_key = get_api_key()
    openai.api_key = api_key
    openai.api_base = base_url + 'v1'
    system_prompt="""   
        1.  用户的系统是: {sys.platform}
        2.  如果用户的输入是命令,帮用户查看命令是否正确，不正确给出正确的命令,最终按照规定输出
            如果用户的输入是自然语言,则帮用户生成命令行，最终按规定输出
        3.  你的输出可以提供多条相关命令供用户选择，最少2条,最多4条,如果没有2条，另外几条可以是类似的命令
        3.  IMPORTANT: 你的输出必须是以下格式, 不准有多余的描述
        <CMD>
        [
            {
                "description": "命令说明",
                "cmd": "命令行"
            },
            {
                "description": "命令说明",
                "cmd": "命令行"
            }
        ]
        </CMD>
    """
    message = [{'role': 'system', 'content': system_prompt}]
    message.append({'role': 'user', 'content': '用户输入: stop main.py, 请严格按照规定输出'})
    message.append({'role': 'assistant', 'content': """
        [
            {
                "description": "停止main.py",
                "cmd": "kill -9 `ps -ef | grep main.py | grep -v grep | awk '{print $2}'`"
            },
            {
                "description": "停止main.py",
                "cmd": "kill $(ps aux | grep 'main.py' | awk '{print $2}')"
            },
            {
                "description": "停止main.py",
                "cmd": "pkill main.py"
            },
            {
                "description": "停止main.py",
                "cmd": "killall main.py"
            }
        ]
    """})
    
    while True:
        user_input = input("请输入命令行或自然语言: ")
        if user_input.strip().lower() == "exit":
            break
        message.append({'role': 'user', 'content': f'用户输入: {user_input}, 请严格按照规定输出'})
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=message,
            temperature=0,
            top_p=1,
            n=1,
            stream=True,
        )
        print("=" * 80)
        tmp = ""
        for resp in response:
            choices = resp.get("choices")
            if not choices:
                continue
            delta = choices[0].get("delta")
            if not delta:
                continue
            if "content" in delta:
                content = delta["content"]
                tmp += content
                # 使用 print_colorful 函数替换原始的 print 函数
                print_colorful(content)
        print()
        print("=" * 80)
        commands = json.loads(tmp.strip())
        print(commands)
        if len(commands) > 0:
            selected_index = select_command(commands)
            # 如果是最后一个，那就是重新输入
            if selected_index == len(commands) - 1:
                continue
            print(f"\n您选择了: {commands[selected_index]['cmd']}")
            # 咨询用户是否执行命令
            if ask_user_execute():
                # 执行命令
                execute_command(commands[selected_index]['cmd'])
                break
            else:
                print("您取消了执行命令")
        else:
            print("没有找到相关命令")
            

# gpterminal.add_command(gpterminal)

if __name__ == '__main__':
    gpterminal()
