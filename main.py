import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import setuptools
import os
import musicLibrary
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Get the API key
api_key = os.getenv("NEWS_API_KEY")


recognizer=sr.Recognizer()


engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_news():
    try:
        # Dynamically format the URL with your API key
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract articles
            articles = data.get('articles', [])
            if not articles:
                speak("No news articles found at the moment.")
                return

            # Speak out the titles of the articles
            speak("Here are the latest news headlines.")
            for article in articles[:5]:  # Limit to 5 articles to avoid overwhelming the user
                title = article.get('title', 'No title available')
                speak(title)
        else:
            speak("Sorry, I couldn't fetch the news at the moment.")
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        speak("Something went wrong while fetching the news.")
        print(f"Exception: {e}")

def processCommand(command):
        c=command.lower()
        if "open google" in c:
            speak("Roger that!")
            webbrowser.open("https://www.google.com")
        elif "open linkedin" in c:
            speak("Roger that!")
            webbrowser.open("https://www.linkedin.com")
        elif "open youtube" in c:
            speak("Roger that!")
            webbrowser.open("https://www.youtube.com")
        elif "open chatgpt" in c:
            speak("Roger that!")
            webbrowser.open("https://www.chatgpt.com")
        elif "open instagram" in c:
            speak("Roger that!")
            webbrowser.open("https://www.instagram.com")
        elif "open amazon" in c:
            speak("Roger that!")
            webbrowser.open("https://www.amazon.com")
        elif "play" in c.lower():
            speak("Roger that!")
            song=c.lower().split(" ")[1]
            link=musicLibrary.music[song]
            webbrowser.open(link)

        elif "news" in c.lower():
            speak("Roger that!")
            get_news()

        else:
            #let openAI handle the request
            pass

if __name__== "__main__":
    speak("Initializing Jarvis...")
    while True:
    #Listen For the wake word "Jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using Google
        # print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source,timeout=5,phrase_time_limit=5)
                word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yo wassap bro!")
                print("Jarvis Active...")

                #Listen for command
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    print(command)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")

