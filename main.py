import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import time
import pywhatkit
import threading  
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    time.sleep(1)
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Shaswat boss. How can I assist you today?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Timeout occurred, please try again.")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why couldn't the bicycle stand up by itself? It was two-tired.",
        "Parallel lines have so much in common. It's a shame they'll never meet."
    ]
    joke = random.choice(jokes)
    speak(joke)


def get_exercise_info(exercise_name, muscle):
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
    headers = {'X-Api-Key': 'mNN8t82cBmE5rTEkCqKnjw==Da8gfu4h5CawPWzO'}  # Replace with your actual API key
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            print("Error:", response.status_code, response.text)
            return None
    except Exception as e:
        print("Error fetching exercise info:", e)
        return None

def get_fitness_info():
    speak("What exercise would you like to know about?")
    exercise_name = take_command().lower()
    muscle = 'biceps'  # Sample muscle, replace with user input19
    exercise_data = get_exercise_info(exercise_name, muscle)
    if exercise_data:
        # Process exercise data here
        print(exercise_data)
    else:
        speak("Sorry, I couldn17't retrieve exercise information at the moment.")

def get_crypto_price():
    symbol = 'LTCBTC'
    api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol)
    headers = {'X-Api-Key': 'mNN8t82cBmE5rTEkCqKnjw==Da8gfu4h5CawPWzO'}  # Replace with your actual API key
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("Error fetching crypto price:", e)

def send_whatsapp_message():
    speak("Whom do you want to send the message to?")
    recipient = take_command().lower()
    speak("What message would you like to send?")
    message = take_command()
    speak("At what hour do you want to send the message?")
    hour = int(input("Enter hour: "))
    speak("At what minute do you want to send the message?")
    minute = int(input("Enter minute: "))
    pywhatkit.sendwhatmsg(recipient, message, hour, minute)
    speak("Message sent successfully!")


def set_alarm():
    hour = int(input("At what hour do you want to set the alarm? Enter hour (0-23): "))
    while not (0 <= hour < 24):
        print("Invalid input. Please enter a valid hour (0-23).")
        hour = int(input("At what hour do you want to set the alarm? Enter hour (0-23): "))
    
    minute = int(input("At what minute do you want to set the alarm? Enter minute (0-59): "))
    while not (0 <= minute < 60):
        print("Invalid input. Please enter a valid minute (0-59).")
        minute = int(input("At what minute do you want to set the alarm? Enter minute (0-59): "))
        
        
limit = 3
api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'mNN8t82cBmE5rTEkCqKnjw==Da8gfu4h5CawPWzO'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

    current_time = datetime.datetime.now()
    alarm_time = datetime.datetime(current_time.year, current_time.month, current_time.day, hour, minute)
    
    time_difference = alarm_time - current_time
    if time_difference.total_seconds() < 0:
        # If the specified time is in the past, adjust it for the next day
        alarm_time += datetime.timedelta(days=1)
        time_difference = alarm_time - current_time
    
    time.sleep(time_difference.total_seconds())
    speak("Time's up!")


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Public\\Music\\Sample Music'  # Change this to your music directory
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif 'talk in hindi' in query:
            engine.setProperty('voice', voices[1].id)  # Change voice to Hindi
            speak("अब मैं हिंदी में बोलूँगा")

        elif 'tell me a joke' in query:
            tell_joke()

        elif 'send whatsapp message' in query:
            send_whatsapp_message()

        elif 'set alarm' in query:
            alarm_thread = threading.Thread(target=set_alarm)
            alarm_thread.start()
            
        elif 'fitness info' in query:
            get_fitness_info()
            
        elif 'crypto price' in query:
            get_crypto_price()
            
        elif 'dadjokes' in query:
            speak("Here are some dad jokes for you:")
            print(response.text)
            speak(response.text)
            
        
        elif 'exit' in query:
            speak("Exiting boss. Goodbye!")
            break
