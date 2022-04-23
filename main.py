import wikipedia
import speech_recognition as sr

import webbrowser as wb

def speak(Text):
    import pyttsx3

    engine = pyttsx3.init()
    engine.say(Text)
    engine.runAndWait()

def Time():
    import datetime

    hour = datetime.datetime.now().hour
    clock = datetime.datetime.now().strftime("%I:%M:%S")

    if hour >= 6 and hour <12: speak(f'Good Morning, it is currently {clock}')

    elif hour >= 12 and hour < 18 : speak(f'Good Afternoon it is currently {clock}')

    elif hour >= 18 and hour < 24 : speak(f'Good Evening it is currently {clock}')

    elif hour >= 24 and hour < 6 : speak(f'Burning the midnight oil are we?. The time is {clock}')


def Date():
    import datetime

    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    today = datetime.datetime.now().day
    speak(f'Hello Your Highness, today is the {today}th ')



def Greetings():
    speak('Welcome Back ')



def command():

    #Class Object for Recognizer with its own Methods

    r = sr.Recognizer()

    #Class Object for Microphone import with its own input

    with sr.Microphone() as source:

        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing.....')
        query = r.recognize_google(audio, language='en-in')


    except Exception as e:
        print(e)
        speak("Say it again please....")

        return 'NONE'
    return query




if __name__ == '__main__':
    Greetings()
    while True:

        query = command().lower()
        if 'chrome' or 'google' in query:
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak('What, would you like to Search')
            search = command().lower()
            wb.get(chromepath).open_new_tab(search.lower() + '.com')

        if 'time' in query :
            Time()
        elif 'date' in query :
            Date()
        elif 'wikipedia' in query:

            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'quit'  in query:
            speak('Good Bye Your Highness , Hit me Up, anytime')
            break
