import os
import sys
from pynput import keyboard
from rich import print
from rich.panel import Panel
from rich.align import Align
import signal


def exit_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

if os.name == "posix":
    import termios
    import tty

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
elif os.name == "nt":
    import msvcrt

    def getch():
        return msvcrt.getch().decode()

options = ["Option 1", "Option 2", "Option 3", "Option 4"]
selected_index = 0

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def select_command(commands):
    selected_index = 0
    # 给最后一个命令加上重新输入
    commands.append({"description": "重新输入", "cmd": "重新输入"})

    def display_commands(commands, selected_index):
        os.system("cls" if os.name == "nt" else "clear")
        hide_cursor()
        aligned = Align.left("\n".join([
            f"[{'>' if i == selected_index else ' '}][dim]{cmd['description']}[/dim]\n  [bold green]{cmd['cmd']}[/bold green]"
            for i, cmd in enumerate(commands)
        ]), vertical="middle")
        panel = Panel(aligned)
        print(panel, end="\r")


    def update_selection(key):
        nonlocal selected_index

        if key == "A":  # Up arrow
            selected_index = (selected_index - 1) % len(commands)
        elif key == "B":  # Down arrow
            selected_index = (selected_index + 1) % len(commands)

    display_commands(commands, selected_index)

    while True:
        key = getch()
        if ord(key) == 27:  # Escape character
            key = getch()
            if key == "[":  # CSI
                key = getch()
                update_selection(key)
                display_commands(commands, selected_index)
        elif key == "\r":  # Enter key
            show_cursor()
            break

    return selected_index

if __name__ == "__main__":
    # 示例用法
    commands = [
        {"des": "这是一个说明1", "cmd": "这是命令1"},
        {"des": "这是一个说明2", "cmd": "这是命令2"},
        {"des": "这是一个说明3", "cmd": "这是命令3"},
        {"des": "这是一个说明4", "cmd": "这是命令4"}
    ]

    selected_index = select_command(commands)
    print(f"\n您选择了: {commands[selected_index]}")

