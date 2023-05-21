# GPTerminal

GPTerminal is a command line tool based on GPT models, designed to help users solve various programming problems by providing intelligent Q&A and code execution features.

## Features

1. Chatting: chat intelligently with GPT-3 or GPT-4.
2. Git CLI assistant: provide Git command help based on your questions.
3. Code execution: execute commands and capture error output and its context, and provide intelligent solutions.

## Installation

Make sure you have Python 3.6 or higher installed. Then run:

```bash
pip install gpterminal

or

pip install gpterminal -i https://pypi.org/simple/ 
```

## Usage

Type the following command in the terminal to start gpterminal:

```bash
gpterminal
```

Then choose the feature you want to use.

### Usage of gt

1. Chatting

   ```
   gt chat
   ```

2. Git CLI assistant

   ```
   gt git
   ```

3. Code execution

   ```
   gt run your-command
   ```


If you type the `gt` command in the terminal and get a `Command not found` prompt, this may be because your system has not added the `gt` command to the PATH environment variable. In this case, you can follow these steps:

### On macOS or Linux

1. Open a terminal and type the following command:

   ```
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   ```

   This adds a line to your `.bashrc` file that adds the `~/.local/bin` directory to the PATH environment variable.

2. Then, reload your `.bashrc` file:

   ```bash
   source ~/.bashrc
   ```

   You should now be able to use the `gt` command in the terminal.

### On Windows

1. Open a command prompt and type the following command:

   ```batch
   setx PATH "%USERPROFILE%\AppData\Roaming\\PythonXX\Scripts;%PATH%"
   ```

   Note that you should replace `PythonXX` with your Python version number, such as `Python36` or `Python39`.

2. Then, close and reopen the command prompt, or log out and log back in to your Windows account.

   You should now be able to use the `gt` command in the command prompt.

### Usage of gs

1. Open a terminal, type `gs`, and press Enter to start GPTTerminal.
2. Enter a command line or natural language prompt as prompted. For example: `compress folder`.
3. GPTTerminal generates multiple related command line codes based on your input, which are displayed on the screen for you to choose from.
4. Use the up and down arrow keys to select the command line code that you think is most appropriate, and press Enter to confirm.
5. The system will ask you whether to execute the selected command. Enter `Y` or `n` to decide whether to execute.
6. If you choose to execute the command, GPTTerminal will execute the command line code you selected.
7. To exit GPTTerminal, type `exit` and press Enter.

## Example

Here is an example of using GPTTerminal:

```
$ gs
Please enter a command line or natural language prompt: compress folder
│ [>] Compress the test folder using zip                                                        
│   zip -r test.zip test                                                         
│ [ ] Compress the test folder using tar                                                        
│   tar -czvf test.tar.gz test          
│ [ ] Enter again    
│   Enter again
```

In this example, the user enters `compress folder`, and GPTTerminal generates two related command line codes and displays them on the screen. The user uses the up and down arrow keys to select the `zip` command to compress the folder, and then presses Enter to confirm. Then, the system asks the user whether to execute the selected command, and the user enters `Y`. GPTTerminal executes the corresponding command.

## Notes

- GPTTerminal is developed based on the GPT-3.5 model. Although it can generate many useful command line codes, it cannot guarantee that all generated codes are correct. Before executing a command, make sure you understand its meaning and possible impact.
- When using GPTTerminal, it is recommended that you operate in a secure environment to prevent data loss or other issues caused by misoperations.

## Issues

1. An API key (required) and base_url (optional) need to be set.
2. If an API key is required, you can wait patiently. I will modify the way of obtaining the API key in the code so that everyone can use it directly.
3. I am still developing the specific way to obtain the free API key, and will update it later. Please stay tuned.
4. If you have any questions, you can raise them in the issues section. I will reply as soon as possible. If you think it's good, you can give me a star, and then you can ask me for a free API key.
5. The reverse endpoint of the free API key has been developed, and you can add my WeChat ID as a friend to request it.
6. The usage limit of the free API key is 2000 times per day for GPT-3.5 and 500 times per day for GPT-4.
7. The free API key has no rate limit, but please do not abuse it.
8. If you need a larger usage quota, you can contact me, and I can provide a paid API key. You can also ask me for it by adding my WeChat ID as a friend.
9. 我的微信号是luzhipeng

## Contribution

Contributions to GPTerminal are welcome! Please make sure your code meets the project's quality standards before submitting a pull request.

## License

GPTerminal is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.