
# AIML-Based Talkback bot

This Python-based talkback robot acts as a personal assistant, capable of engaging in conversations, performing tasks, and providing helpful information. Powered by Artificial Intelligence Markup Language (AIML), it can greet you, respond to your queries, tell the time, open applications, and search the web. The robot can also translate into a few select languages, making it versatile in day-to-day use.

## Features:
- **Conversational Responses**: The robot can greet you, engage in small talk, and respond to a wide range of questions.
- **Time Queries**: Ask for the current time, and the assistant will provide the exact time.
- **Application Launcher**: It can open common applications on your system (e.g., browser, calculator, notepad) via voice commands.
- **Web Search**: The robot can search the web for any query, acting like a search engine assistant.
- **Translation**: Supports translations in a select few languages, making it a helpful tool for quick language conversions.

## Project Structure:
- `new1.py`: The final version of the project, which includes enhanced functionalities like telling the time and language translation.
- `aiml_data/`: This folder contains the AIML files, defining the responses and patterns for interaction.
- `requirements.txt`: A list of required dependencies to run the assistant.

## How it Works:
The robot is built on AIML for its conversational abilities and uses Python libraries to extend functionality like opening applications, searching the web, and fetching the current time. The assistant listens to user commands, processes them using AIML patterns, and responds accordingly.

## Libraries Used:
- **AIML**: For defining chatbot conversational patterns.
- **datetime**: For providing time-related information.
- **os**: To interface with the operating system and open applications.
- **webbrowser**: For performing web searches.
- **googletrans**: For language translation.

## How to Use:
1. Clone the repository and install the required dependencies from `requirements.txt`.
2. Run `new1.py` to start interacting with the talkback robot.
3. Ask the robot to perform tasks such as telling the time, opening applications, or searching the web.
4. Use the translation feature by asking the assistant to translate a word or phrase into a supported language.

## Example Commands:
- "Hello!"
- "What time is it?"
- "Open notepad."
- "Search the web for Python tutorials."
- "Translate 'hello' into Spanish."

