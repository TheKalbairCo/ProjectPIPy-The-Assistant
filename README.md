

# AIML-Based Talkback Bot- PIPy(Predictive Intelligence in Python)

This Python-based talkback bot functions as a personal assistant, capable of engaging in conversations, performing tasks, and providing useful information. Powered by Artificial Intelligence Markup Language (AIML), the bot can greet you, respond to queries, tell the time, open applications, and search the web. It also includes a translation feature for a few select languages, adding more versatility to its capabilities.

## Features:
- **Conversational Abilities**: The bot can greet, engage in small talk, and respond to a variety of questions.
- **Time Queries**: It can tell you the current time upon request.
- **Application Launcher**: Use voice commands to open common applications like browsers, notepads, and calculators.
- **Web Search**: The bot can search the web based on your queries, acting as an assistant for information retrieval.
- **Translation**: Translate words or phrases into a few supported languages with ease.

## Project Structure:
- `new1.py`: The final version of the bot, featuring time-telling and translation functionalities.
- `aiml_data/`: Contains AIML files, defining the patterns and responses for interaction.
- `requirements.txt`: Lists the dependencies required to run the bot.

## How it Works:
The bot is built using AIML to manage conversations and Python libraries to extend its functionality. It listens to user input, matches it against AIML patterns, and performs the corresponding action—whether it's opening an app, fetching the time, or conducting a web search.

## Libraries Used:
- **AIML**: For defining conversation patterns and responses.
- **datetime**: To provide the current time.
- **os**: To interact with the operating system for opening applications.
- **webbrowser**: For conducting web searches.
- **googletrans**: For language translation.

## How to Use:
1. Clone the repository and install the dependencies listed in `requirements.txt`.
2. Run `new1.py` to start interacting with the bot.
3. Ask the bot to perform various tasks, such as telling the time, opening applications, or searching the web.
4. Use the translation feature to convert words or phrases into supported languages.

## Example Commands:
- "Hi there!"
- "What time is it?"
- "Open the calculator."
- "Search for Python programming tutorials."
- "Translate 'good morning' into French."
