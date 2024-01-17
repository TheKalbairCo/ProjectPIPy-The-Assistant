import webbrowser
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
from googletrans import Translator
from gtts import gTTS
import playsound

translator = Translator()

def speak(audio):
    print('sam: ' + audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('output.mp3')
    playsound.playsound('output.mp3')
    os.remove('output.mp3')

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')

greetMe()

speak('hai')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        lang = r.recognize_google(audio, language='ml-IN')
        print('User: ' + lang + '\n')
        result = translator.translate(lang, src="ml", dest="en")
        lang = result.text
    except sr.UnknownValueError:
        speak('Sorry! Please try again.')
        lang = myCommand()
        result = translator.translate(lang, src="en", dest="ml")
        lang = result.text
    return lang

if __name__ == '__main__':

    while True:
        lang = myCommand()
        lang = lang.lower()
        if 'open youtube' in lang:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in lang:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'open gmail' in lang:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif "what\'s up" in lang or 'how are you' in lang:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif 'nothing' in lang or 'abort' in lang or 'stop' in lang:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'hello' in lang:
            speak('Hello Sir')
        elif 'say english alphabets' in lang or 'english alphabet' in lang:
            Alphabet()
        elif 'bye' in lang:
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'play music' in lang:
            music_folder = 'Your_music_folder_path'
            music = ['music1', 'music2', 'music3', 'music4', 'music5']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            speak('Okay, here is your music! Enjoy!')
        else:
            lang = lang
            speak('Searching...')
            try:
                try:
                    res = client.lang(lang)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                except:
                    results = wikipedia.summary(lang, sentences=1)
                    speak(results)
                    results = translator.translate(results, src="en", dest="ml")
                    mal = results.text
                    speak(mal)
            except:
                speak('I don\'t know, Sir! Google is smarter than me!')

