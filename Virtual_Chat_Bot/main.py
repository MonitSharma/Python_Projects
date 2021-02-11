import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def Hello():
    speak(""" Hello Sir, I am your Laptop Assistant, Tell me How Can I help You""")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language="en-in")
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say That Again")
            return "None"
        return Query


def Take_query():
    Hello()
    while (True):
        query = takeCommand().lower()
        if "hello how are you" in query:
            speak("I am Fine")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
        elif "bye" in query:
            speak("Thank You, Next")
            exit()
        elif "from Wikipedia" in query:
            speak("checking the website ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(result)
        elif "tell me your name" in query:
            speak(" I am Nick, Your laptop assistant")


if __name__ == '__main__':
    Take_query()
