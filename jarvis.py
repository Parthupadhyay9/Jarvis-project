import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
from requests import get
import pyjokes
import time
import pyautogui
import requests
import pytz
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('VX54WV-WYAQQPX9UE')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)


def date():
    t_date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
    speak(t_date.strftime('%d %B, %Y'))


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\sirvi\\OneDrive\\Desktop\\parth\\jarvisScreenshot\\js.png")
    speak("I have taken the screenshot.")


def greetMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        speak(f"Good Morning!, its {tt}")

    if hour >= 12 and hour < 18:
        speak(f"Good Afternoon!, its {tt}")

    if hour >= 18 and hour != 0:
        speak(f"Good Evening!, its {tt}")


greetMe()
speak('Hello Sir, I am your digital assistant Jarvis!')
speak('How may I help you?')


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dd1997ff09d849d98c53cab34f0b0655'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = takeCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'voice' in query:
            greetMe()

        elif 'open google' in query:
            speak('sir what should I search on google')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'screenshot' in query:
            screenshot()

        elif 'open avachara' in query:
            speak('okay')
            webbrowser.open('www.avachara.com')

        elif 'date' in query:
            date()

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'document' in query:
            speak('okay')
            webbrowser.open('https://docs.google.com/document/u/0/')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!',
                      'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! The time is {strTime}")

        elif 'remember' in query:
            speak("What Should I write down sir")
            note = takeCommand()
            remember = open("data.txt", "w")
            remember.write(note)
            remember.close()
            speak("I have noted that " + note)

        elif 'what are my reminders' in query:
            remember = open('data.txt', 'r').read()
            speak("You told me to remember that " + remember)

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = takeCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = takeCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login('parth.u@outlook.com', 'Parth@123')
                    server.sendmail('parth.u@outlook.com',
                                    'parth.capt@gmail.com', content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak(
                        'Sorry Sir! I am unable to send your message at this moment!For now Try typing your mail by yourself')
                    webbrowser.open(
                        'https://mail.google.com/mail/u/0/#inbox?compose=new')

        elif 'play music' in query:
            music_folder = 'C:\\Users\\sirvi\\Music\\'
            music = ['music', 'music1', 'music2', 'music3', 'music4',
                     'music5', 'music6', 'music7', 'music8', 'music9', 'music10']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            speak('Okay, here is your music! Enjoy!')
        elif 'open code' in query:
            codePath = "C:\\Users\\sirvi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open robot' in query:
            codePath = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
            os.startfile(codePath)

        elif 'srishti' in query:
            codePath = "C:\\Users\\sirvi\\OneDrive\\Desktop\\Srishti"
            os.startfile(codePath)

        elif 'word' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        elif 'settings' in query:
            codePath = "%windir %\\System32\\Control.exe"
            os.startfile(codePath)

        elif 'edge' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)

        elif 'excel' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)

        elif 'nice' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(codePath)

        elif 'firefox' in query:
            codePath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(codePath)

        elif 'studio' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Enterprise\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)

        elif 'visio' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\VISIO.EXE"
            os.startfile(codePath)

        elif 'publisher' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSPUB.EXE"
            os.startfile(codePath)

        elif 'adobe' in query:
            codePath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(codePath)

        elif 'access' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
            os.startfile(codePath)
        elif'open notepad' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.Lnk"
            os.startfile(codePath)

        elif 'close notepad' in query:
            speak("OK sir! closing notepad")
            os.system("taskkill /f /im notepad.Lnk")

        elif 'tell me news' in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 12:
                music_folder = "C:\\Users\\sirvi\\Music"
                songs = os.listdir(music_folder)
                os.startfile(os.path.join(music_folder, songs[0]))

        elif 'tell me a joke' in query or 'one more' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shutdown' in query:
            os.system("shutdown /s /t 5")

        elif 'restart' in query:
            os.system("shutdown /r /t 5")

        elif 'sleep' in query:
            os.system("rundll32.exe powrporf.dll, setSuspendState 0,1,0")

        elif 'command prompt' in query:
            os.system("start cmd")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"yout IP address is {ip}")
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')
