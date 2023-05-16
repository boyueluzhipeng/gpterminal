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

### 示例

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


## 问题
1. 需要设置api_key(必填)以及base_url(可选)
2. 需要 api_key 的也可以耐心等待，后续我会修改代码中获取 api_key 的方式，可以让大家直接使用
3. 具体免费 api_key 的获取方式我还在开发中，后续会更新，敬请期待

## 贡献

欢迎对 GPTerminal 进行贡献！请在提交 Pull Request 之前确保您的代码符合项目的质量标准。

## 许可

GPTerminal 采用 MIT 许可证。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。



