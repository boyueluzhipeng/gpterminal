import subprocess
import click

import requests
from .ChatGPT import Chatbot
import os
import sys
from rich.live import Live
from rich.markdown import Markdown
from .code_execution import *
import yaml
from pathlib import Path

sys.stdin.reconfigure(encoding='utf-8')

@click.command()
def hello():
    """Say hello"""
    click.echo('Hello, world!')

@click.group()
def gpterminal():
    """Figlu command line tool"""
    # 默认调用bash函数
    pass


def chatgpt_explanation(api_key, base_url, language, error_message, model, maxtoken):
    query = construct_query(language, error_message)
    chatbot = Chatbot(api_key=api_key, base_url=base_url, engine=model, max_tokens=maxtoken)
    res = chatbot.ask_stream(query)
    return res


def get_api_key():
    # 确定配置文件的存储位置
    config_path = Path.home() / ".config" / "GPTerminal" / "config.yaml"

    # 检查配置文件是否存在，如果不存在则提示用户创建
    if not config_path.is_file():
        print(f"Config file not found at {config_path}.")
        # 创建配置文件所在的目录
        config_path.parent.mkdir(parents=True, exist_ok=True)
        # 创建配置文件
        config_path.touch()
        while True:
            api_key = input("Please enter your OpenAI API key: ").strip()
            if api_key:
                break
            else:
                print("API key cannot be empty. Please try again.")
        while True:
            base_url = input("Please enter the OpenAI API base URL (or leave blank): ").strip()
            if base_url or base_url == "":
                break
            else:
                print("Base URL cannot be empty. Please try again.")

        # 将 API key 和 base URL 写入配置文件
        with open(config_path, "w") as f:
            yaml.safe_dump({"api_key": api_key, "base_url": base_url or None}, f)
    else:
        #读配置文件中的 API key 和 base URL
        with open(config_path) as f:
            config = yaml.safe_load(f)
            api_key = config.get("api_key", None)
            base_url = config.get("base_url", None)

    # 如果没有读取到 API key，则引发异常
    if not api_key:
        raise Exception("Please enter OpenAI API key in the config file.")

    return base_url, api_key




@click.command()
@click.option("--model", default="gpt-3.5-turbo", help="Specify which GPT model to use")
@click.option("--maxtoken", default=4096, help="Maximum number of tokens in a single prompt")
def chat(model, maxtoken):
    """Chat with GPT-3 or GPT-4"""
    base_url, api_key = get_api_key()
    bot = Chatbot(api_key=api_key, base_url=base_url, engine=model, max_tokens=maxtoken)
    while True:
        text = input("You: ")
        if text.strip() == "exit":
            break
        response = bot.ask_stream(text)
        md = Markdown("")
        with Live(md, auto_refresh=False) as live:
            tmp = ""
            for r in response:
                tmp += r
                md = Markdown(tmp)
                live.update(md, refresh=True)
                

@click.command()
@click.option("--model", default="gpt-3.5-turbo", help="Specify which GPT model to use")
@click.option("--maxtoken", default=4096, help="Maximum number of tokens in a single prompt")
def git(model, maxtoken):
    """问问关于git的问题"""
    print("这是一个git命令行助手,你可以通过这个助手来学习git命令")
    # use openai to generate git scripts
    base_url, api_key = get_api_key()
    bot = Chatbot(api_key=api_key, base_url=base_url, system_prompt="""
    你是一个很好的git命令行助手，你可以帮助我更好的使用git, 
    根据我的问题,你可以给我提供一些git命令
    """, engine=model, max_tokens=maxtoken)
    while True:
        text = input("请输入你的问题: ")
        if text.strip() == "exit":
            break
        response = bot.ask_stream(text)
        print("=" * 80)
        tmp = ""
        for r in response:
            tmp += r
            print(r, end='', flush=True)
        print()
        print("=" * 80)
            
            
            
@click.command()
@click.argument('args', nargs=-1)
@click.option("--model", default="gpt-3.5-turbo", help="Specify which GPT model to use")
@click.option("--maxtoken", default=4096, help="Maximum number of tokens in a single prompt")
@click.option("--lines", default=100, help="Number of lines before and after the error to capture as context")
def run(args, model, maxtoken, lines):
    """
    接收不固定参数的命令，并执行它们。如果发生错误，将捕获并显示错误输出及其上下文。
    """
    try:
        base_url, api_key = get_api_key()
        language = get_language(args)
        # 将参数元组转换为列表，并将其传递给subprocess.run函数
        result = subprocess.run(
            list(args), stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        # 找出可能涉及的文件
        source_files = [arg for arg in args if os.path.isfile(arg)]
        file_contents = []

        for file in source_files:
            # 检查文件字数是否超过2000
            num_chars = os.stat(file).st_size
            if num_chars <= 2000:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
            else:
                with open(file, 'r', encoding='utf-8') as f:
                    head_lines = [next(f, '') for _ in range(lines)]
                with open(file, 'r', encoding='utf-8') as f:
                    tail_lines = [line for _, line in zip(range(lines), f.readlines())]
                    

                content = "".join(head_lines) + "\n...\n" + "".join(tail_lines)

            file_contents.append(content)

        # 获取错误输出
        error_output = e.stderr
        
        # 打印错误输出
        click.echo(error_output)

        # 将文件内容与错误输出合并
        total_input = f"Error Output:\n{error_output}\n\n"
        for i, content in enumerate(file_contents):
            total_input += f"File Content ({source_files[i]}):\n{content}\n\n"

        # 使用GPT模型处理整个输入
        with LoadingMessage():
            response = chatgpt_explanation(api_key, base_url, language, total_input, model, maxtoken)

        # 使用Rich库将结果显示为Markdown
        md = Markdown("")
        with Live(md, auto_refresh=True) as live:
            tmp = ""
            for r in response:
                tmp += r
                md = Markdown(tmp)
                live.update(md, refresh=True)
    else:
        click.echo(result.stdout)
    

gpterminal.add_command(hello)
gpterminal.add_command(chat)
gpterminal.add_command(git)
gpterminal.add_command(run)

if __name__ == '__main__':
    gpterminal()
