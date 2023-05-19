
[中文README](README_CN.md)
# GPTerminal

GPTerminal is a command-line tool based on the GPT model, designed to help users solve various programming problems, providing intelligent Q&A and code execution functions.

## Features

1. Chatting: Smart chat with GPT-3 or GPT-4.
2. Git CLI Assistant: Provide Git command help based on your questions.
3. Code Execution: Execute commands and capture error output and their context, providing intelligent solutions.

## Installation

Make sure you have Python 3.6 or higher installed. Then run:

```bash
pip install gpterminal

or

pip install gpterminal -i https://pypi.org/simple/ 
```

## Usage

Enter the following command in the terminal to start gpterminal:

```bash
gpterminal
```

Then choose the feature you want to use.

### gt Usage

1. Chatting

   ```
   gt chat
   ```

2. Git CLI Assistant

   ```
   gt git
   ```

3. Code Execution

   ```
   gt run your-command
   ```

If you get the message `Command not found` when you enter the `gt` command in the terminal, it may be because your system has not added the `gt` command to the PATH environment variable. In this case, you can follow these steps:

### On macOS or Linux

1. Open a terminal and enter the following command:

   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   ```

   This will add a line to your `.bashrc` file that adds the `~/.local/bin` directory to the PATH environment variable.

2. Then, reload your `.bashrc` file:

   ```bash
   source ~/.bashrc
   ```

   Now you should be able to use the `gt` command in the terminal.

### On Windows

1. Open a command prompt and enter the following command:

   ```batch
   setx PATH "%USERPROFILE%\AppData\Roaming\\PythonXX\Scripts;%PATH%"
   ```

   Note that you should replace `PythonXX` with your Python version number, such as `Python36` or `Python39`.

2. Then, close and reopen the command prompt, or log out and log back in to your Windows account.

   Now you should be able to use the `gt` command in the command prompt.

## gs Usage

1. Open a terminal, enter `gs`, and press Enter to start GPTTerminal.
2. Enter a command line or natural language according to the prompt. For example: `compress folder`.
3. GPTTerminal will generate multiple related command-line codes based on your input, displayed on the screen for you to choose from.
4. Use the up and down arrow keys to select the command-line code that you think is most appropriate, and press Enter to confirm.
5. The system will ask you whether to execute the command. Enter `Y` or `n` to decide whether to execute.
6. If you choose to execute the command, GPTTerminal will execute the command-line code you selected.
7. To exit GPTTerminal, enter `exit` and press Enter.

## Example

Here is an example of using GPTTerminal:

```
$ gs
Please enter a command line or natural language: compress folder
│ [>]Compress the test folder using zip                                                       
│   zip -r test.zip test                                                                      
│ [ ]Compress the test folder using tar                                                       
│   tar -czvf test.tar.gz test                                                                 
│ [ ]Re-enter                                                                                 
│   Re-enter
```

In this example, the user entered `compress folder`, and GPTTerminal generated two related command-line codes, which were displayed on the screen. The user selected to compress the folder using the `zip` command using the arrow keys, and then pressed Enter to confirm. Then, the system asked the user whether to execute the selected command, and the user entered `Y`. GPTTerminal executed the corresponding command.

## Notes

- GPTTerminal is developed based on the GPT-3.5 model. Although it can generate many useful command-line codes, it cannot guarantee that all generated codes are correct. Before executing a command, please make sure you understand the meaning of the command and its possible effects.
- When using GPTTerminal, it is recommended that you operate in a secure environment to prevent data loss or other issues caused by misoperations.

## Issues
1. api_key (required) and base_url (optional) need to be set.
2. For those who need api_key, please be patient. I will modify the way to obtain api_key in the code later, so that everyone can use it directly.
3. I am still developing the specific way to obtain a free api_key, and will update it later. Please stay tuned.

## Contributing

Contributions to GPTerminal are welcome! Please ensure that your code meets the project's quality standards before submitting a Pull Request.

## License

GPTerminal is licensed under the MIT license. For more information, see the [LICENSE](LICENSE) file.
