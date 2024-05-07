### Discord Message Automation Scripts

These scripts allow you to automate sending messages on Discord channels. You can either send messages with a timer between them or send a series of messages with different intervals.

#### Requirements
- Python 3.x
- Discord Token (2020 but sill works - https://www.youtube.com/watch?v=YEgFvgg7ZPI)
- Discord Channel ID (https://www.youtube.com/watch?v=NLWtSHWKbAI)

#### Installation
1. Clone or download this repository to your local machine.

2. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

3. Edit the `config.json` file to add your Discord channel ID, Discord bot token, and message content as per your requirements.

#### Usage

##### Script 1: Single Message with Timer

1. Open the `main.py` file in a text editor or code editor (VS Code, Codium, Vim and other).

2. Modify the `config.json` file to set your Discord channel ID, Discord bot token, and the message content. You can also set the interval at which the message will be sent. The last solo interval is the reset time for the message loop/reset to first.

3. Save your changes.

4. Run the script by executing:
    ```
    python main.py
    ```
    
    or
    
    ```
    py main.py
    ```    
    or
    
    ```
    py3 main.py
    ```

   This script will continuously send the specified message to the Discord channel with the provided interval (in seconds).

##### Script 2: Multiple Messages with Different Intervals

1. Open the `main.py` file in a text editor or code editor (VS Code, Codium, Vim and other).

2. Modify the `config.json` file to set your Discord channel ID, Discord bot token, and messages with their respective intervals.

3. Save your changes.

4. Run the script by executing:
    ```
    python main.py
    ```
    
    or
    
    ```
    py main.py
    ```    
    or
    
    ```
    py3 main.py
    ```

   This script will send each message from the configured list with its specified interval to the Discord channel.

#### Important Notes
- Make sure your account has the necessary permissions to send messages in the specified channel.
- The provided interval is in seconds. Adjust it according to your requirements (e.g. 3600 seconds = 60 minutes = 1 hour).
- Ensure that your account token and channel ID are kept secure. Do not share them publicly.
- I am not responsible for the use of the code by third parties, regardless of the reason. Therefore, in case of misuse or proper use, I bear no responsibility for its use by third parties.

#### Security
- Do not share your Discord bot token with anyone.
- Do not share your Discord channel ID with anyone.
- Do not share your `config.json` file with anyone.
- Please ensure that your credentials, such as your account Token and Channel ID, are not visible to other individuals or online automated systems. You and only you have access to them, and if you inadvertently expose them publicly on any repository or anywhere on the internet, it is entirely your responsibility.

Feel free to reach out if you encounter any issues or have any questions!