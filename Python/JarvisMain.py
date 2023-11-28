import speech_recognition as sr
from gtts import gTTS
import os
import openai
import numpy as np
# from JarvisArrays import *
import sys
import cwd 
cwd.cwd(".txt")


def chat_with_bot(prompt, lang):
    openai.api_key = "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"
    try:
        print("GPT is processing...")
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": f"You are a helpful assistant. You answer in this language:{lang} "},
                {"role": "user", "content": f"{prompt}"}
            ], 
        )
    except Exception as ex:
        print(f"Was unable to proess using prompt: {prompt}, and language: {lang}. Error:{str(ex)}")
    response = response.choices[0].message['content'].strip()
    print(response)
    return response


def speech_to_text(lang):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    while True:
        with microphone as source:
            print("\nListening...")
            audio = recognizer.listen(source)

        try:
            print("Trying to process...")
            text = recognizer.recognize_google(audio, language=lang)
            print(f"Text recognized: {text}")
            return text
        except sr.UnknownValueError:
            print(f"Was unable to process while using language {lang}...")
            continue
        except sr.RequestError:
            print("Sorry, there was an error connecting to the Google API.")
            sys.exit()
            

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False, )
    tts.save("Chat.mp3")

with open("vocabulary.txt") as file:
    text = file.read()
    text_to_speech(text, "fr")


# if __name__ == "__maiin__":
#     print("""Jarvis, a AI project by Mihail Zabolotnic
#         (michail.zabolotnic@gmail.com)""")
    
#     lang_SST = language_codes[input("Select language for SST:  ").strip().lower()]
#     lang_TTS = language_codes[input("Select language for TTS:  ").strip().lower()]
#     lang_GPT = input("Select language for GPT:  ")


#     while True:

#         user_message = speech_to_text(lang=lang_SST)
#         response = chat_with_bot(prompt=user_message, lang=lang_GPT)
#         text_to_speech(text=response, lang=lang_TTS)
#         input(":")
    





response = openai.Image.create(
  prompt="a dungeon map for dnd",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)