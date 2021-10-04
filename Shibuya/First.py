import os
import smtplib
import webbrowser
import pyttsx3
import wikipedia
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!") 

    speak("I am KUZURI . Please tell me how may I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("donald.laish@gmail.com","donald200310394062")
    server.sendmail("donald.laish@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Google")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play video' in query:
            video_dir="C:\\Users\\Donald\\Videos\\New folder"
            video=os.listdir(video_dir)
            print(video)
            os.startfile(os.path.join(video_dir,video[0]))
        elif 'this time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            codePath= "C:\\Users\\Donald\\Desktop\\kuzuri.AI\\Shibuya\\First.py"
            os.startfile(codePath)
        elif 'email to me' in query:
            try:
                speak('What Should I do for you ?')
                content = takeCommand()
                to = "someone@gamil.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ! email wasn't sent" + "Try after some times.")




