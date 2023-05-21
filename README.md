# GPTerminal

GPTerminal 是一个基于 GPT 模型的命令行工具，旨在帮助用户解决各种编程问题，提供智能问答和代码执行功能。

## 功能

1. 聊天：与 GPT-3 或 GPT-4 进行智能聊天。
2. Git 命令行助手：根据您的问题提供 Git 命令帮助。
3.代码执行：执行命令并捕获错误输出及其上下文，提供智能解决方案。

## 安装

确保安装 Python 3.6 或更高版本。然后运行：

```bash
pip install gpterminal

或者

pip install gpterminal -i https://pypi.org/simple/ 
```

## 使用

在命令行中输入以下命令启动 gpterminal

```bash
gpterminal
```

然后选择您想要使用的功能。

### gt 使用方法

1. 聊天

   ```
   gt chat
   ```

2. Git 命令行助手

   ```
   gt git
   ```

3. 代码执行

   ```
   gt run your-command
   ```


当您在终端中输入 `gt`令时，如果提示 `Command not found`，这可能是因为您的系统未将 `gt` 命令添加到 PATH 环境变量中。在这种情况下，您可以按照以下步骤操作：

### 在 macOS 或 Linux 上

1. 打开终端并输入以下命令：

   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   ```

   这将向您的 `.bashrc` 文件添加一行，该行将 `~/.local/bin` 目录添加到 PATH 环境变量中。

2. 然后，重新加载您的 `.bashrc` 文件：

   ```bash
   source ~/.bashrc
   ```

   现在，您应该能够在终端中使用 `gt` 命令了。

### 在 Windows 上

1. 打开命令提示符并输入以下命令：

   ```batch
   setx PATH "%USERPROFILE%\AppData\Roaming\\PythonXX\Scripts;%PATH%"
   ```

   请注意，将 `PythonXX` 替换为您的 Python 版本号，例如 `Python36` 或 `Python39`。

2. 然后，关闭并重新打开命令提示符，或者注销并重新登录您的 Windows 帐户。

   现在，您应该能够在命令提示符中使用 `gt` 命令了。

## gs使用方法

1. 打开终端，输入 `gs` 并回车，启动 GPTTerminal。
2. 根据提示，输入命令行或自然语言。例如：`压缩文件夹`。
3. GPTTerminal 会根据您的输入生成多个相关的命令行代码，显示在屏幕上，供您选择。
4. 使用方向键上下选择您认为最合适的命令行代码，按回车确认。
5. 系统会询问您是否要执行该命令，输入 `Y` 或 `n` 决定是否执行。
6. 如果您选择执行命令，GPTTerminal 会执行您选择的命令行代码。
7. 若要退出 GPTTerminal，输入 `exit` 并回车。

## 示例

以下是一个使用 GPTTerminal 的示例：

```
$ gs
请输入命令行或自然语言: 压缩文件夹
│ [>]使用zip压缩test文件夹                                                        
│   zip -r test.zip test                                                         
│ [ ]使用tar压缩test文件夹                                                        
│   tar -czvf test.tar.gz test          
│ [ ]重新输入    
│   重新输入
```

在这个示例中，用户输入了`压缩文件夹`，GPTTerminal 生成了两个相关的命令行代码，并显示在屏幕上。用户使用方向键选择了使用 `zip` 命令压缩文件夹，然后按回车确认。接着，系统询问用户是否执行选择的命令，用户输入 `Y`，GPTTerminal 执行了相应的命令。

英文README.md[README_EN.md](README_EN.md)
## 注意事项

- GPTTerminal 是基于 GPT-3.5 模型开发的，虽然它可以生成很多有用的命令行代码，但不能保证所有生成的代码都是正确的。在执行命令前，请确保您了解命令的含义和可能的影响。
- 在使用 GPTTerminal 时，建议您在一个安全的环境中进行操作，以防止因误操作导致的数据丢失或其他问题。


## 问题
1. 需要设置api_key(必填)以及base_url(可选)
2. 需要 api_key 的也可以耐心等待，后续我会修改代码中获取 api_key 的方式，可以让大家直接使用
3. 具体免费 api_key 的获取方式我还在开发中，后续会更新，敬请期待
4. 有任何问题可以在 issues 中提出，我会尽快回复，如果觉得不错，可以给我一个star，然后可以找我要一个免费的 api_key
5. 免费api_key的反向端点已经开发完成，大家可以通过添加我的微信号好友找我索要
6. 免费api_key的使用限量是每日gpt3.5 2000次的使用以及， gpt4每日500次的调用
7. 免费api_key是没有速率限制的，但是请大家不要滥用
8. 如果需要更大的调用量，可以联系我，我可以提供付费的api_key，都可以通过添加我的微信号好友找我索要

## 贡献

欢迎对 GPTerminal 进行贡献！请在提交 Pull Request 之前确保您的代码符合项目的质量标准。

## 许可

GPTerminal 采用 MIT 许可证。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。



