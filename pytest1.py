import speech_recognition as sr
from gtts import gTTS
import os
import requests
import playsound
import webbrowser
import random
import wikipedia
import datetime
import wolframalpha
import sys
from googletrans import Translator
from langdetect import detect

translator = Translator()

recognizer = sr.Recognizer()
client = wolframalpha.Client('RVE8T3-YKWR64492V')

def speak(audio):
    tts = gTTS(text=audio, lang="en")
    tts.save("output.mp3")
    os.system("afplay output.mp3")
    print('Pipy: ' + audio)
    #engine.say(audio)
    #engine.runAndWait()


def greetMe():
    with sr.Microphone() as source:
        print("Initializing...")
        currentH = int(datetime.datetime.now().hour)
    try:
        if currentH >= 0 and currentH < 12:
            speak('Good Morning! Abhi, how can i help you today?')

        if currentH >= 12 and currentH < 18:
            speak('Good Afternoon! Abhi, how can i help you?')

        if currentH >= 18 and currentH != 0:
            speak('Good Evening!Abhi, how can i help you ?')
    finally:
            pass

greetMe()
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        recognized_lang = r.recognize_google(audio)
        detected_lang = detect(recognized_lang)
        print("Detected language:", detected_lang)

        if detected_lang == 'ml':
            lang = r.recognize_google(audio, language="ml-IN")
            print('User: ' + lang + '\n')

            op = translator.translate(lang, src="ml-IN", dest="en-US")
            translated_text = op.text
            print("Pipy:", translated_text)
            return translated_text
        else:
            print("Invalid source language:", detected_lang)
            speak("Sorry, I cannot translate from this language.")
            return ""

    except sr.UnknownValueError:
        speak('Sorry, please try again.')
        return ""


def listen():
    if __name__== '_main_':

     while True:

        translated_text = myCommand()
        translated_text = translated_text.lower()

        if 'open youtube' in translated_text:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in translated_text:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in translated_text:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in translated_text or 'how are you' in translated_text:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))


        elif 'nothing' in translated_text or 'abort' in translated_text or 'stop' in translated_text:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in translated_text:
            speak('Hello Sir')

        elif 'say english alphabets' in translated_text or 'english alphabet' in translated_text:
            Alphabet()

        elif 'bye' in translated_text:
            speak('Bye Sir, have a good day.')
            sys.exit()


            speak('Okay, here is your music! Enjoy!')


        else:
            translated_text = translated_text
            speak('Searching...')
            try:
                try:
                    res = client.translated_text(translated_text)
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
                speak('I don\'t know Sir! Please rephrase and try again!')

        speak('Waiting for Next Command...')
try:
    op = translator.translate(lang, dest="en").text.lower()
except Exception as e:
    print("Translation error:", e)

while True:
    myCommand()
    listen()
