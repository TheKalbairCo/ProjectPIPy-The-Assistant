import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
import random
import wikipedia
import datetime
import wolframalpha
import sys
from googletrans import Translator
import langid
import subprocess
import pyautogui
import requests

translator = Translator()

recognizer = sr.Recognizer()
client = wolframalpha.Client('RVE8T3-YKWR64492V')

def speak(audio):
    tts = gTTS(text=audio, lang="en")
    tts.save("output.mp3")
    os.system("afplay output.mp3")
    print('Pipy: ' + audio)

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def greetMe():
    with sr.Microphone() as source:
        print("Initializing...")
        currentH = int(datetime.datetime.now().hour)
    try:
        if currentH >= 0 and currentH < 12:
            speak('Good Morning! Abhi, how can I help you today?')
        elif currentH >= 12 and currentH < 18:
            speak('Good Afternoon! Abhi, how can I help you?')
        elif currentH >= 18 and currentH != 0:
            speak('Good Evening! Abhi, how can I help you?')
    finally:
        pass

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "Did you hear about the claustrophobic astronaut? He needed a little space.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call a fake noodle? An impasta!"
        # Add more jokes to the list if you want
    ]

    joke = random.choice(jokes)

    speak(joke)


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.phrase_time_limit = 5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        recognized_lang = r.recognize_google(audio)
        detected_lang, _ = langid.classify(recognized_lang)

        print("Detected language:", detected_lang)

        if detected_lang == 'ml':
            lang = r.recognize_google(audio, language="ml-IN")
            print('User: ' + lang + '\n')

            op = translator.translate(lang, src="ml", dest="en")
            translated_text = op.text
            print("Pipy (Malayalam):", translated_text)
            return translated_text
        elif detected_lang == 'en':
            lang = r.recognize_google(audio, language="en")
            print('User: ' + lang + '\n')
            print("Pipy (English):", lang)
            return lang
        else:
            print("Invalid source language:", detected_lang)
            speak("Sorry, I cannot translate from this language.")
            return ""

    except sr.UnknownValueError:
        speak('Sorry, please try again.')
        return ""

def screenshot():
    img = pyautogui.screenshot()
    file_path ="/Users/abhimanyuvenu/Dropbox/Mac/Downloads/ss3.png"
    img.save(file_path)
    return file_path



def read_news_headlines(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']
        headlines = [article['title'] for article in articles]

        counter=0
        for index, headline in enumerate(headlines, start=1):
            print(f"Headline {index}: {headline}")
            speak(headline)

            counter+=1
            if counter==5:
                break
    else:
        print("Failed to fetch news. Check your API key or connection.")

api_key = 'bd343f33963740269bf5345090fe8cd6'

if api_key != 'bd343f33963740269bf5345090fe8cd6':
    read_news_headlines(api_key)
else:
    print("")

def listen():
    if __name__ == '__main__':
        while True:
            translated_text = myCommand()
            translated_text = translated_text.lower()

            if 'open youtube' in translated_text:
                speak('Okay')
                webbrowser.open('https://www.youtube.com/')

            elif "who are you" in translated_text or "what are you" in translated_text or "whats your name" in translated_text:
                speak("I'm Pipy,short for predictive intelligence on Python ,An A.I Assistant created by Mr. Abhimanyu. ")
                print("I'm PIPY(Predictive Intelligence on PYthon),An A.I Assistant created by Mr. Abhimanyu.")

            elif 'open google' in translated_text:
                speak('Okay')
                webbrowser.open('https://www.google.com/')

            elif 'open gmail' in translated_text:
                speak('Okay')
                webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

            elif "open" in translated_text:
                app_name = translated_text.replace("open ", "")  # Extract the app name from the query
                try:
                    subprocess.run(["open", "-a", app_name])
                    speak(f"Opening {app_name}")
                except Exception as e:
                    print(e)
                    speak(f"Sorry, I couldn't open {app_name}.")

            elif "what's up" in translated_text or 'how are you' in translated_text or 'how you doing' in translated_text:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))

            elif "hi pipy" in translated_text or 'hello pipy' in translated_text or 'hi pipi' in translated_text or 'hello pipi' in translated_text or 'hi BP' in translated_text or 'hello hippie' in translated_text or 'high BP' in translated_text or 'hippie' in translated_text:
                stMsgs = ['Hi Abhi,How can i help you today', 'Hey,How can i assist you today', 'Hello sir,how can i help you today', 'Hey there,How can i help you']
                speak(random.choice(stMsgs))

            elif 'nothing' in translated_text or 'abort' in translated_text or 'stop' in translated_text:
                speak('Okay')
                speak('Bye Sir, have a good day.')
                sys.exit()

            elif 'hello' in translated_text:
                speak('Hello Sir')

            elif "time" in translated_text or "what time is it" in translated_text:
                time()

            elif "date" in translated_text or "what is today's date" in translated_text:
                date()

            elif 'say english alphabets' in translated_text or 'english alphabet' in translated_text:
                Alphabet()

            elif 'bye' in translated_text:
                speak('Bye Sir, have a good day.')
                sys.exit()

            elif 'crack a joke' in translated_text:

                tell_joke()

            elif 'read latest news' in translated_text or 'read news' in translated_text or 'news' in translated_text:
                read_news_headlines(api_key)

            elif "search on chrome" in translated_text or "search" in translated_text or "search using chrome" in translated_text:
                try:
                    speak("What should I search?")
                    print("What should I search?")
                    search = listen()
                    search_url = "https://www.google.com/search?q=" + search

                    subprocess.run(["open", "-a", "Google Chrome", search_url])
                    print(search)
                except Exception as e:
                    print(e)

            elif "play music" in translated_text or "play a song" in translated_text:
                song_dir = "/Users/abhimanyuvenu/Music/Music/Media.localized/Music/Unknown Artist/Unknown Album"  # Update the path to your music directory
                songs = os.listdir(song_dir)
                print(songs)

                if songs:
                    y = random.randint(0, len(songs) - 1)
                    song_path = os.path.join(song_dir, songs[y])
                    subprocess.run(["open", song_path])
                else:
                    speak("No music files found")
                    print("No music files found in the directory.")

            elif "offline" in translated_text:
                quit()

            elif "take a screenshot" in translated_text:
                file_path = screenshot()
                speak("I've taken a screenshot, opening it now")

                subprocess.run(["open", file_path])

            else:
                translated_text = translated_text
                speak('Searching on the internet...')
                try:
                    try:
                        res = client.query(translated_text)
                        results = next(res.results).text
                        speak('WOLFRAM-ALPHA says - ')
                        speak('Got it.')
                        speak(results)

                    except:
                        results = wikipedia.summary(translated_text, sentences=1)
                        speak(results)
                        results = translator.translate(results, src="en", dest="ml")
                        mal = results.text
                        speak(mal)

                except:
                    speak('I didnt\'t get that! Please rephrase and try again!')
                    continue
            speak('Waiting for the Next Command...')


greetMe()
listen()
