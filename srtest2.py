import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import sys
from googletrans import Translator
from langdetect import detect

translator = Translator()

engine = pyttsx3.init('nsss')

client = wolframalpha.Client('RVE8T3-YKWR64492V')

voices = engine.getProperty('voices')
engine.setProperty('rate', 170)

engine.setProperty('voice', voices[1].id)


def speak(audio):
    print('Pipy: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning! Abhi, how can i help you today?')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon! Abhi, how can i help you?')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!Abhi, how can i help you ?')


greetMe()
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        recognized_lang = r.recognize_google(audio)
        detected_lang = detect(recognized_lang)
        print("Detected language:", detected_lang)

        lang = detected_lang  # Assigning a default language, such as Malayalam ("ml-IN")
        op = translator.translate(lang, dest="en").text.lower()

        lang = r.recognize_google(audio, language="ml-IN")
        print('User: ' + lang + '\n')

        op = translator.translate(lang, src="ml-IN", dest="en")
        translated_text = op.text
        print("brain:", translated_text)


    except sr.UnknownValueError:
        speak('Sorry ! try again')
    return translated_text


if _name_ == '_main_':

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
                speak('I don\'t know Sir! Google is smarter than me!')

        speak('Next Command!!')

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
        speak('Sorry ! try again')
        lang = myCommand();
        result = translator.translate(lang, src="en", dest="ml")
        lang = result.text

    return lang


if _name_ == '_main_':

    while True:

        lang = myCommand();
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


        else:
            lang = lang
            speak('Searching...')
            try:
                try:
                    results = wikipedia.summary(translated_text)
                    speak(results)
                    results = translator.translate(results, src="en", dest="ml")
                    mal = results.text
                    speak(mal)

                except:
                    res = client.lang(lang)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)


            except:
                speak('I don\'t know Sir! Google is smarter than me!')

        speak('Next Command!!')