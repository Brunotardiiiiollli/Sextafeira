import openai
import pyttsx3
import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")  # Pode alterar para outras vozes disponíveis
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎙️ Ouvindo...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language="pt-BR")
        except:
            return ""

while True:
    user_input = listen()
    print(f"Você disse: {user_input}")
    if not user_input:
        continue
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente de voz que responde chamando o usuário de senhor."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        print("Jarvis:", reply)
        speak(reply)
    except Exception as e:
        print("Erro ao gerar resposta:", e)
        speak("Desculpe, senhor. Não consegui responder.")
