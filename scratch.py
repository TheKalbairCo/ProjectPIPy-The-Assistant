import speech_recognition as sr
from gtts import gTTS
import os
import requests
from bs4 import BeautifulSoup

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")
    os.system("afplay output.mp3")  # macOS-specific command

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I couldn't reach the speech recognition service.")
        return ""

def process_command(command):
    if "reminder" in command:
        speak("Sure! What should I remind you about?")
        reminder_text = listen()
        # Implement your reminder functionality here
        speak(f"Reminder set for: {reminder_text}")
    elif "to-do list" in command:
        speak("Let's create a to-do list. What tasks would you like to add?")
        task_list = []
        while True:
            task = listen()
            if "stop" in task:
                break
            if task:
                task_list.append(task)
        # Implement your to-do list functionality here
        speak("To-do list created!")
    elif "search" in command:
        speak("What would you like to search for?")
        search_query = listen()
        # Perform web search
        url = f"https://www.google.com/search?q={search_query}"
        response = requests.get(url)
        if response.status_code == 200:
            speak(f"Here are the search results for: {search_query}")
            soup = BeautifulSoup(response.text, "html.parser")
            search_results = soup.select(".tF2Cxc")[:3]  # Get the top 3 search results
            for i, result in enumerate(search_results, start=1):
                result_text = result.get_text()
                print(f"Result {i}: {result_text}")
                speak(result_text)
        else:
            speak("Sorry, I couldn't perform the web search.")
    elif "quit" in command or "exit" in command:
        speak("Goodbye!")
        quit()
    else:
        speak("Sorry, I didn't understand that command.")

# Main program loop
speak("Hi, how can I assist you today?")
while True:
    command = listen()
    process_command(command)
