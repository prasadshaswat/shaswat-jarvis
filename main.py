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
import geocoder
import spacy
import win10toast
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from win10toast import ToastNotifier
import cv2
from bs4 import BeautifulSoup


# Load English language model
nlp = spacy.load("en_core_web_sm")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_face():
    cap = cv2.VideoCapture(0)  # Use 0 for the primary camera
    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            print("Face Detected")
            cap.release()
            cv2.destroyAllWindows()
            return True
        else:
            print("No face detected. Retrying...")

        cv2.imshow('img', img)
        
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return False



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

def good_night():
    speak("Good night boss. Have a nice sleep!")
    time.sleep(4)
    os.system("shutdown /s /t 5")
    


def generate_meme(template_id, username, password, text0, text1):
    url = 'https://api.imgflip.com/caption_image'
    params = {
        'template_id': '129242436',
        'username': 'PrasadShaswat',
        'password': '8V!EX7uzHF8vHYg',
        'text0': text0,
        'text1': text1
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            return data['data']['url']
        else:
            return None
    else:
        print("Failed to generate meme. Status code:", response.status_code)
        return None



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
    
def get_location():
    # Get latitude and longitude
    g = geocoder.ip('me')
    lat_lng = g.latlng

    # Get the address from latitude and longitude
    location = geocoder.osm(lat_lng, method='reverse')
    return location.address

def add_work(work, time):
    work_list[work] = time
    speak(f"Work '{work}' added at {time}.")

def remove_work(work):
    if work in work_list:
        del work_list[work]
        speak(f"Work '{work}' removed from the to-do list.")
    else:
        speak(f"Work '{work}' not found in the to-do list.")

def show_works():
    if work_list:
        speak("Here are the works in your to-do list:")
        for work, time in work_list.items():
            speak(f"{work} at {time}.")
    else:
        speak("Your to-do list is empty.")

def manage_works():
    current_time = datetime.datetime.now().strftime("%H:%M")
    for work, time in work_list.items():
        if time == current_time:
            speak(f"It's time for {work}!")
            # You can add further actions here, like opening a webpage or playing music
            # Example: webbrowser.open("https://www.example.com")
            del work_list[work]  # Remove work once it's done


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
    



def get_celebrity_info(name):
    api_url = f'https://api.api-ninjas.com/v1/celebrity?name={name}'
    api_key = 'mNN8t82cBmE5rTEkCqKnjw==Da8gfu4h5CawPWzO'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None
    
def send_email(recipient, subject, body):
    # Email configuration (replace with your SMTP server details)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # For example, 587 for TLS
    sender_email = 'hbvgsjhf@gmail.com'
    sender_password = 'shaswat2031'
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient
    message['Subject'] = subject
    
    # Add body to email
    message.attach(MIMEText(body, 'plain'))
    
    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        
def get_motivational_message():
    try:
        response = requests.get('https://zenquotes.io/api/random')
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q'] + " - " + data[0]['a']
            return quote
        else:
            print("Failed to fetch motivational message. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error fetching motivational message:", e)
        return None



def set_alarm():
    hour = int(input("At what hour do you want to set the alarm? Enter hour (0-23): "))
    while not (0 <= hour < 24):
        print("Invalid input. Please enter a valid hour (0-23).")
        hour = int(input("At what hour do you want to set the alarm? Enter hour (0-23): "))
    
    minute = int(input("At what minute do you want to set the alarm? Enter minute (0-59): "))
    while not (0 <= minute < 60):
        print("Invalid input. Please enter a valid minute (0-59).")
        minute = int(input("At what minute do you want to set the alarm? Enter minute (0-59): "))
        
        
        
def track_amazon_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find(id='productTitle').get_text().strip()
        price = soup.find(id='priceblock_ourprice').get_text().strip()  # Adjust this based on the actual HTML structure
        return title, price
    else:
        print("Failed to fetch Amazon page:", response.status_code)
        return None, None
    
    
    
    
def get_product_price():
    speak("Sure, please provide the Amazon URL of the product.")
    url = input("Enter Amazon product URL: ")  # You can modify this to use voice input
    product_title, product_price = track_amazon_price(url)
    if product_title and product_price:
        speak(f"The price of {product_title} is {product_price}")
    else:
        speak("Sorry, I couldn't fetch the price of the product.")




        
        
limit = 3
api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'mNN8t82cBmE5rTEkCqKnjw==Da8gfu4h5CawPWzO'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

    current_time = datetime.datetime.now()
    alarm_time = datetime.datetime(current_time.year, current_time.month, current_time.day,hour, minute)
    
    time_difference = alarm_time - current_time
    if time_difference.total_seconds() < 0:
        # If the specified time is in the past, adjust it for the next day
        alarm_time += datetime.timedelta(days=1)
        time_difference = alarm_time - current_time
    
    time.sleep(time_difference.total_seconds())
    speak("Time's up!")


if __name__ == "__main__":
    if detect_face():
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

            elif 'open google' in query:
                webbrowser.open("http://google.com")

            elif 'open stack overflow' in query:
                webbrowser.open("http://stackoverflow.com")

            elif 'play music' in query:
                music_dir = 'C:\\Users\\Public\\Music\\Sample Music'  # Adjust to your music directory
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {str_time}")

            elif 'talk in hindi' in query:
                # This assumes `engine` and `voices` have been defined and set up elsewhere
                engine.setProperty('voice', voices[1].id)  # Change to Hindi voice
                speak("अब मैं हिंदी में बोलूँगा")

            elif 'tell me a joke' in query:
                tell_joke()

            elif 'send email' in query:
                # Assume `send_email` is defined elsewhere
                speak("Whom do you want to send the email to?")
                recipient = input("Enter recipient email: ")
                speak("What is the subject of the email?")
                subject = take_command()
                speak("What message would you like to send?")
                body = take_command()
                send_email(recipient, subject, body)
                speak("Email sent successfully!")

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
                speak(response.text)  # Assumes `response` has been defined or obtained from a jokes API

            elif 'add work' in query:
                speak("What work would you like to add?")
                work = take_command().lower()
                speak("At what time would you like to schedule this work?")
                time = take_command()
                add_work(work, time)  # Assumes `add_work` is defined elsewhere

            elif 'remove work' in query:
                speak("What work would you like to remove?")
                work = take_command().lower()
                remove_work(work)  # Assumes `remove_work` is defined elsewhere

            elif 'show works' in query:
                show_works()  # Assumes `show_works` is defined elsewhere

            elif 'manage works' in query:
                manage_works()  # Assumes `manage_works` is defined elsewhere

            elif 'where am i' in query:
                location = get_location()  # Assumes `get_location` is defined elsewhere
                speak(f"You are currently at {location}")
                # Write address to a file
                with open("location.txt", "w") as file:
                    file.write(location)

            elif 'celebrity info' in query:
                speak("Whose information would you like to know?")
                name = take_command().lower()
                celebrity_info = get_celebrity_info(name)  # Assumes `get_celebrity_info` is defined elsewhere
                if celebrity_info:
                    print(celebrity_info)
                    speak(f"Here is some information about {name}: {celebrity_info}")
                else:
                    speak("Sorry, I couldn't retrieve celebrity information at the moment.")

            elif 'open youtube' in query:
                webbrowser.open("http://youtube.com")

            elif 'search and play' in query:
                speak("What would you like to search and play on YouTube?")
                search_query = take_command()
                pywhatkit.playonyt(search_query)

            elif 'motivational message' in query:
                motivational_message = get_motivational_message()  # Assumes this function is defined elsewhere
                if motivational_message:
                    speak(motivational_message)
                    print(motivational_message)
                else:
                    speak("Sorry, I couldn't retrieve a motivational message at the moment.")

            elif 'meme' in query:
                speak("What would you like the meme to say?")
                text0 = take_command()
                speak("What should the second line say?")
                text1 = take_command()
                meme_url = generate_meme('129242436', 'YourUsername', 'YourPassword', text0, text1)  # Assumes implementation
                if meme_url:
                    speak("Here is your meme!")
                    webbrowser.open(meme_url)
                else:
                    speak("Sorry, I couldn't generate a meme at the moment.")

            elif 'good night' in query:
                good_night()  # Assumes `good_night` is defined elsewhere

            elif 'change voice' in query:
                if voices[0].id == engine.getProperty('voice'):
                    engine.setProperty('voice', voices[1].id)
                else:
                    engine.setProperty('voice', voices[0].id)
            
            elif 'product price' in query:
                get_product_price()
                speak("Here is the product price")
                speak(product_price)
          
            elif 'exit' in query:
                speak("Exiting, boss. Goodbye!")
                break  # Correct place for the break statement

