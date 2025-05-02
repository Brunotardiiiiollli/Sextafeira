import openai
import pyttsx3
import speech_recognition as sr
from playsound import playsound
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
       # 🔧 Comandos personalizados do sistema
    if "abrir navegador" in user_input.lower():
        os.system("start chrome")
        speak("Abrindo navegador, senhor.")
        continue

    if "abrir youtube" in user_input.lower():
        os.system("start https://www.youtube.com")
        speak("Abrindo YouTube, senhor.")
        continue

    if "abrir downloads" in user_input.lower():
        os.system("start %HOMEPATH%\\Downloads")
        speak("Abrindo sua pasta de downloads, senhor.")
        continue

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

import openai
import pyttsx3
import speech_recognition as sr
import os
from dotenv import load_dotenv
from playsound import playsound  # Importa o playsound para reproduzir áudio

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Toca a voz personalizada de boas-vindas
playsound("audio/voz_jarvis.mp3")

# Define a chave da API do OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# --------------------------------------------------------
# A partir daqui, o restante do seu código do Jarvis continua.
# Exemplo de função de execução de comando ou inicialização:

def iniciar_assistente():
    print("🔵 Iniciando assistente Jarvis...")
    # Adicione as funcionalidades do seu assistente aqui
    # Exemplo:
    # comando = capturar_comando()  <-- sua função de reconhecimento de voz
    # resposta = processar_comando(comando)
    # print("Resposta:", resposta)
    print("✅ Sistema pronto para comandos.")

if __name__ == "__main__":
    iniciar_assistente()
