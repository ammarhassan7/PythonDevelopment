import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
from config import apikey
import datetime
import subprocess
import random

# Set OpenAI API key
openai.api_key = apikey

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Ammar: {query} \nJarvis: \n\n"
    try:
        # Use the supported model `gpt-3.5-turbo` for chat completions
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure this is the correct model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": chatStr}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        
        # Get the response text
        answer = f"{response.choices[0].message['content'].strip()} \n"  # Adjusted for ChatCompletion
        say(answer)
        chatStr += f"Jarvis: {answer}\n"
        return answer
        
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Please check your quota and billing details.")
        # Optional: Retry after some time

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")

def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n ************************************** \n\n"
    
    try:
        # Use the supported model `gpt-3.5-turbo`
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Update this to the latest model if available
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        
        # Get the response text
        answer = response.choices[0].text.strip()  # Use `.strip()` to remove extra whitespace
        print(answer)
        text += answer

        # Ensure the "Openai" directory exists
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        # Save the response to a file in the "Openai" directory
        with open(f"Openai/prompt-{random.randint(1, 23344444)}.txt", "w") as f:
            f.write(text)
    
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Please check your quota and billing details.")
        # Optional: Retry after some time
        

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")



def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

say("Hello, I am Jarvis")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing Command...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Some Error Occurred, Sorry! from Jarvis")
            return ""

while True:
    print("Listening....")
    query = takeCommand()
    
    sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"]]
    
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} boss...")
            webbrowser.open(site[1])
    
    if "open music" in query:
        print("Opening music...")
        musicPath = r"E:\Python Practice\Music App\Music Player\music\Nasheeds\a-thousand-greetings.mp3"
        os.startfile(musicPath)

    elif "the time" in query:
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"Sir the time is {strfTime}")

    elif "open camera" in query.lower():
        say("Opening Camera...")
        subprocess.run("start microsoft.windows.camera:", shell=True)
 
    elif "open spotify" in query.lower():
        say("Opening Spotify...")
        subprocess.run("start spotify:", shell=True)

    elif "using artificial intelligence" in query.lower():
        ai(prompt=query)

    elif "Jarvis Quit".lower() in query.lower():
        exit()
    
    elif "Reset Chat".lower() in query.lower():
        chatStr = ""

    else:
        print("Jarvis is Listening...")
        chat(query)
