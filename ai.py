# -*- coding: utf-8 -*-
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import pyttsx3  # синтез речи (Text-To-Speech)
import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой
import g4f
from g4f.Provider import (
Bing,
AiChatOnline,
HuggingChat,
Liaobots,
)
import settings as plugin
 


a = """
░██████╗░█████╗░░██████╗██╗░░██╗░█████╗░  ██╗░░░██╗░█████╗░██╗░█████╗░███████╗ ███╗░░░███╗░█████╗░██████╗░███████╗
██╔════╝██╔══██╗██╔════╝██║░░██║██╔══██╗  ██║░░░██║██╔══██╗██║██╔══██╗██╔════╝ ████╗░████║██╔══██╗██╔══██╗██╔════╝
╚█████╗░███████║╚█████╗░███████║███████║  ╚██╗░██╔╝██║░░██║██║██║░░╚═╝█████╗░░ ██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░
░╚═══██╗██╔══██║░╚═══██╗██╔══██║██╔══██║  ░╚████╔╝░██║░░██║██║██║░░██╗██╔══╝░░ ██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░
██████╔╝██║░░██║██████╔╝██║░░██║██║░░██║  ░░╚██╔╝░░╚█████╔╝██║╚█████╔╝███████╗ ██║░╚═╝░██║╚█████╔╝██████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░╚═╝░╚════╝░╚══════╝ ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝
                                            
                                                    by Rufinds
"""
print(a)

class VoiceAssistant:
    """
    Настройки голосового ассистента, включающие имя, пол, язык речи
    """
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""


def setup_assistant_voice():
    """
    Установка голоса по умолчанию (индекс может меняться в 
    зависимости от настроек операционной системы)
    """
    voices = ttsEngine.getProperty("voices")
    assistant.recognition_language = "ru-RU"
    # Microsoft Irina Desktop - Russian
    ttsEngine.setProperty("voice", voices[plugin.voice_settings()].id)


def play_voice_assistant_speech(text_to_speech):
    """
    Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    :param text_to_speech: текст, который нужно преобразовать в речь
    """
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=plugin.voice_noise())

        try:
            print("Listening...")
            play_voice_assistant_speech('Слушаю вас')
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            play_voice_assistant_speech('Проверьте микрафон')
            return

        # использование online-распознавания через Google 
        # (высокое качество распознавания)
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит 
        # попытка использовать offline-распознавание через Vosk
        except speech_recognition.RequestError:
            print("Trying to use offline recognition...")


        return recognized_data



if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()

    # настройка данных голосового помощника
    assistant = VoiceAssistant()
    assistant.name = "Sasha"
    assistant.sex = "female"
    assistant.speech_language = "ru"

    # установка голоса по умолчанию
    setup_assistant_voice()

    while True:
        
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input)

        play_voice_assistant_speech(plugin.func(voice_input=voice_input))
input()