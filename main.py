import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon")

    else:
        speak("good evening")

    speak("How   are   you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 578)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
      query = takeCommand().lower()


      if 'wikipedia' in query:
          speak('Searching wikipedia')
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=2)
          speak('According to wikipedia')
          print(results)
          speak(results)


      elif 'open youtube' in query:
          webbrowser.open('youtube.com')

      elif 'open google' in query:
          webbrowser.open('google.com')

      elif 'time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"The time is {strTime}")

      elif 'suits' in query:
          speak('opening suits')
          webbrowser.open('https://i.redd.it/bndw3jh4l0d61.png')

      elif 'email' in query:
          try:
              speak('What should I say?')
              content = takeCommand()
              to = ""
              sendEmail(to, content)
              speak("email has been sent")
          except Exception as e:
              print(e)
              speak("I am sorry I can not send this email")

      elif 'how are you' in query:
          speak("I am good too, thank you. ")



