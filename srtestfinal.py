import speech_recognition as sr
from gtts import gTTS
import os
import requests
import playsound
from bs4 import BeautifulSoup

# Initialize the speech recognition engine
recognizer = sr.Recognizer()
def set_reminder(reminder_text):
    # Code to set a reminder goes here
    print("Reminder set:", reminder_text)

    # Convert the reminder text to speech
    tts = gTTS(text="Reminder set: " + reminder_text, lang="en")
    tts.save("reminder.mp3")
    playsound.playsound("reminder.mp3")


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
            search_results = soup.find_all("div", class_="r")
        for result in search_results:
            title = result.find("h3").text
            link = result.find("a")["href"]
            print("Title:", title)
            print("Link:", link)
            print()
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
