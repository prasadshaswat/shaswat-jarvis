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
import ctypes
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



# Load English language model
nlp = spacy.load("en_core_web_sm")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#add feature on when pc is on or reboot


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











conversation_memory = {}

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
        # Store the conversation in memory
        conversation_memory[query] = "I heard you say: " + query
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

#open chrome and do speedtest in fast.com
def speed_test():
    speak("Opening Chrome and running speed test. Please wait.")
    webbrowser.open("https://fast.com")
    time.sleep(180)  # Wait for 60 seconds for the test to complete
    speak("Speed test completed. Closing Chrome.")
    os.system("taskkill /im chrome.exe /f")  # Close Chrome after the test
    

def finger_count():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)

        # Threshold the image to get binary image
        _, binary = cv2.threshold(gray_blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            hull = cv2.convexHull(max_contour, returnPoints=False)
            defects = cv2.convexityDefects(max_contour, hull)

            # Count the number of defects
            if defects is not None:
                count = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    far = tuple(max_contour[f][0])
                    if d > 10000:  # Adjust this threshold based on your hand size
                        count += 1
                        cv2.circle(frame, far, 3, [255, 0, 0], -1)
                cv2.putText(frame, str(count + 1), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("Finger Count", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    
            
def random_talks():
    speak("Sure, let's have a random conversation. You can ask me anything.")
    while True:
        query = take_command().lower()
        if 'exit' in query:
            speak("Ending the random conversation.")
            break
        else:
            response = respond(query)
            print(response)
            speak(response)


def wolfram_alpha(query):
    app_id = "LA925J-VA7E8YQR47"  # Replace with your actual Wolfram Alpha App ID
    base_url = "http://api.wolframalpha.com/v1/spoken?appid={}&i={}"
    try:
        response = requests.get(base_url.format(app_id, query))
        if response.status_code == 200:
            # The response text is now the answer in spoken form.
            answer = response.text
            speak(answer)
            print("Wolfram Alpha response:", answer)
        else:
            print("Failed to fetch Wolfram Alpha response:", response.status_code)
            speak("Sorry, I couldn't fetch the response from Wolfram Alpha.")
    except Exception as e:
        print("An error occurred:", e)
        speak("An error occurred while fetching the response.")


def respond(query):
    # Add logic to respond based on the query
    # You can use conversation_memory to generate replies
    # For example:
    if query in conversation_memory:
        return conversation_memory[query]
    else:
        return "I'm sorry, I didn't catch that."


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


def distance_calculator():
    origin_input = input("Enter the origin address: ")
    destination_input = input("Enter the destination address: ")
    api_key = '5b3ce3597851110001cf6248ff078824ef1743d2ab893ed17e8a2e4a'  # Replace with your actual ORS API key

    # ORS uses a different parameter format, so we first need to geocode the addresses
    geocode_url = 'https://api.openrouteservice.org/geocode/search'
    headers = {
        'Authorization': api_key
    }
    # Geocode origin
    response_origin = requests.get(geocode_url, headers=headers, params={'text': origin_input})
    if response_origin.status_code != 200:
        print("Failed to geocode origin address")
        return
    origin_coords = response_origin.json()['features'][0]['geometry']['coordinates']
    
    # Geocode destination
    response_destination = requests.get(geocode_url, headers=headers, params={'text': destination_input})
    if response_destination.status_code != 200:
        print("Failed to geocode destination address")
        return
    destination_coords = response_destination.json()['features'][0]['geometry']['coordinates']
    
    # Now that we have coordinates, we can use them to find the distance and duration
    directions_url = 'https://api.openrouteservice.org/v2/directions/driving-car'
    params = {
        'start': f'{origin_coords[0]},{origin_coords[1]}',
        'end': f'{destination_coords[0]},{destination_coords[1]}'
    }
    response = requests.get(directions_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        distance = data['features'][0]['properties']['segments'][0]['distance'] / 1000  # Distance in kilometers
        duration = data['features'][0]['properties']['segments'][0]['duration'] / 60  # Duration in minutes
        distance_text = f"The distance between {origin_input} and {destination_input} is {distance:.2f} kilometers."
        duration_text = f"The duration to travel from {origin_input} to {destination_input} is {duration:.2f} minutes."
        print(distance_text)
        print(duration_text)
        speak(distance_text)
        speak(duration_text)
    else:
        print("Failed to fetch distance and duration:", response.status_code)



def gesture_control():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)

        # Threshold the image to get binary image
        _, binary = cv2.threshold(gray_blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            epsilon = 0.0005 * cv2.arcLength(max_contour, True)
            approx = cv2.approxPolyDP(max_contour, epsilon, True)
            hull = cv2.convexHull(max_contour)

            cv2.drawContours(frame, [hull], 0, (0, 255, 0), 2)

            # Calculate the center of the palm
            M = cv2.moments(max_contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)

                # Calculate the angle of the hand
                angle = math.atan2(approx[0][0][1] - approx[2][0][1], approx[0][0][0] - approx[2][0][0])
                angle = angle * 180 / math.pi

                # Volume Up gesture
                if 60 < abs(angle) < 120:
                    ctypes.windll.user32.keybd_event(0xAF, 0, 0, 0)  # Volume Up key code
                    cv2.putText(frame, "VOL UP", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # Volume Down gesture
                elif abs(angle) > 150:
                    ctypes.windll.user32.keybd_event(0xAE, 0, 0, 0)  # Volume Down key code
                    cv2.putText(frame, "VOL DOWN", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Gesture Control", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def count_faces():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) > 0:
            print(f"Number of faces detected: {len(faces)}")
            speak(f"Number of faces detected: {len(faces)}")
        else:
            print("No faces detected.")
            speak("No faces detected.")
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    


    
def fetch_recent_cricket_matches():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

    headers = {
        "X-RapidAPI-Key": "4c9b78c691msh97368a3c7ae2607p1f5585jsnd15998f8ab42",  # Replace YOUR_API_KEY_HERE with your actual RapidAPI Key
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        print(response.json())  # Print the JSON response
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

# Call the function to fetch recent cricket matches

    

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

work_list = {}  # Define an empty dictionary to store work and time mappings

def add_work(work, time):
    global work_list  # Use the global keyword to modify the global variable
    work_list[work] = time
    speak(f"Work '{work}' added at {time}.")

def remove_work(work):
    global work_list
    if work in work_list:
        del work_list[work]
        speak(f"Work '{work}' removed from the to-do list.")
    else:
        speak(f"Work '{work}' not found in the to-do list.")

def show_works():
    global work_list
    if work_list:
        speak("Here are the works in your to-do list:")
        for work, time in work_list.items():
            speak(f"{work} at {time}.")
    else:
        speak("Your to-do list is empty.")

def manage_works():
    global work_list
    current_time = datetime.datetime.now().strftime("%H:%M")
    for work, time in work_list.items():
        if time == current_time:
            speak(f"It's time for {work}!")
            # You can add further actions here, like opening a webpage or playing music
            # Example: webbrowser.open("https://www.example.com")
            del work_list[work]  # Remove work once it's done

# The rest of your code remains unchanged



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
    
#click photo using webcam and save destop
def click_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('C:\\Users\\Public\\Desktop\\webcam.jpg', frame)
        cap.release()
        cv2.destroyAllWindows()
        speak("Photo clicked and saved on desktop.")
    else:
        speak("Failed to click photo. Please try again.")

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
        
        
        
        
        
#random animal sound api
def get_animal_sound():
    response = requests.get('https://api.api-ninjas.com/v1/animalsound')
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
        
        
        
        
def love_calculator():
    name1 = input("Enter your name: ")
    name2 = input("Enter your partner's name: ")
    url = f'https://love-calculator.p.rapidapi.com/getPercentage?fname={name1}&sname={name2}'
    headers = {
        "X-RapidAPI-Key": "4c9b78c691msh97368a3c7ae2607p1f5585jsnd15998f8ab42",  # Replace with your actual RapidAPI Key
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == requests.codes.ok:
        data = response.json()
        print(f"Love percentage between {name1} and {name2} is {data['percentage']}%")
        speak(f"Love percentage between {name1} and {name2} is {data['percentage']}%")
    else:
        print("Failed to fetch love percentage:", response.status_code)
        
        
        
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
    
def weather():
    api_key = "fcde9f54650c3a1dcaa942bd95d6be21"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))
    else:
        print(" City Not Found ")
        
    
    
def get_product_price():
    speak("Sure, please provide the Amazon URL of the product.")
    url = input("Enter Amazon product URL: ")  # You can modify this to use voice input
    product_title, product_price = track_amazon_price(url)
    if product_title and product_price:
        speak(f"The price of {product_title} is {product_price}")
    else:
        speak("Sorry, I couldn't fetch the price of the product.")



def google_search(query):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the snippet result. This might need to be updated based on Google's HTML structure changes
        snippet = soup.find('div', class_='BNeawe').text
        return snippet
    else:
        return "I'm sorry, I couldn't fetch the results from Google."

#chatgpt using api
def chat_gpt(query):
    url = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Authorization": "Bearer sk-4c9b78c691msh97368a3c7ae2607p1f5585jsnd15998f8ab42",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": query,
        "max_tokens": 100
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise exception for HTTP errors
        result = response.json()
        if 'choices' in result and result['choices']:
            return result['choices'][0]['text']
        else:
            print("No completion choices available.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
    
    

        
        
#hindi jokes
def hindi_jokes():
    jokes = [
        "डॉक्टर: आपकी आंखें ठीक हैं, आपको चश्मा क्यों लगाना पड़ रहा है? पेशेवर: डॉक्टर साहब, आपकी आंखें ठीक हैं, आपको चश्मा क्यों लगाना पड़ रहा है?",
        "टीचर: तुम्हारे पास एक गोलू है, एक गोलू और एक गोलू, तो तुम्हारे पास क्या है? छात्र: खाली जगह, सर।",
        
        
    ]
    joke = random.choice(jokes)
    speak(joke)
    



def funny_jokes():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why couldn't the bicycle stand up by itself? It was two-tired.",
        "Parallel lines have so much in common. It's a shame they'll never meet."
        "Why did the math book look sad? Because it had too many problems.",
        
    ]
    joke = random.choice(jokes)
    speak(joke)
    
    


def fetch_programming_memes():
    url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

    headers = {
        "X-RapidAPI-Key": "4c9b78c691msh97368a3c7ae2607p1f5585jsnd15998f8ab42",
        "X-RapidAPI-Host": "programming-memes-images.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch programming memes:", response.status_code)
        return None

memes_data = fetch_programming_memes()



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
            elif 'count face' in query:
                count_faces()
            elif 'click photo' in query:
                click_photo()
                
            elif 'programming meme' in query:
                meme = random.choice(memes_data)
                meme_url = meme['url']
                speak("Here is a programming meme for you!")
                webbrowser.open(meme_url)
                
            elif 'google' in query:
                speak("What would you like to search on Google?")
                search_query = take_command()
                google_result = google_search(search_query)
                speak(google_result)
                print(google_result)
                
            elif 'wolf' in query:
                speak("What would you like to ask Wolfram Alpha?")
                question = take_command()
                wolfram_alpha(question)
                
          
                
                

            elif 'open google' in query:
                webbrowser.open("http://google.com")

            elif 'open stack overflow' in query:
                webbrowser.open("http://stackoverflow.com")
                
            elif 'finger count' in query:
                finger_count()

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
            elif 'funny joke' in query:
                funny_jokes()
                
            elif 'chat' in query:
                speak("Sure, what would you like to chat about?")
                chat_query = take_command()
                chat_response = chat_gpt(chat_query)
                if chat_response:
                    print(chat_response)
                    speak(chat_response)
                else:
                    speak("Sorry, I couldn't generate a response at the moment.") 
                        
            elif 'hindi joke' in query:
                speak("Here is a Hindi joke for you!")
                hindi_jokes()
                
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


            elif 'add work' in query:
                speak("What work would you like to add?")
                work = take_command()
                speak("At what time?")
                time = take_command()
                add_work(work, time)
                
            elif 'remove work' in query:
                speak("What work would you like to remove?")
                work = take_command()
                remove_work(work)
                   
            elif 'random_talk' in query:
                random_talks()

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
                    
            elif 'speed_test' in query:
                speed_test()

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
                
                
            elif 'volume control' in query:
                gesture_control()
                speak("Gesture control ended")
                
            elif 'face ' in query:
                detect_face()
                speak("Face detected")
                
            elif 'click photo' in query:
                click_photo()
                speak("Photo clicked and saved on desktop.")
                
            elif 'animal sound' in query:
                #which animal
                get_animal_sound()
            
                
            elif 'weather' in query:
                speak("Here is the weather information")
                speak("what is the city name")
                weather()
                
            
                
            elif 'love calculator' in query:
                love_calculator()
                speak
                
           
            
                
            elif 'distance ' in query:
                speak("Here is the distance information")
                
                distance_calculator()
        
            elif 'exit' in query:
                speak("Exiting, boss. Goodbye!")
                break 

