import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = " "  # Replace with your real key

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message['content']

while True:
    command = listen()
    if command.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye!")
        break
    response = chat_with_gpt(command)
    print("AI:", response)
    speak(response)
