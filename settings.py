# -*- coding: utf-8 -*-
# Функция для выбора голоса #
import g4f
from g4f.Provider import (
HuggingChat,
Pizzagpt,
DDG
#Сюда добавлять модели с g4f через запятую
)
import sys
import asyncio
import os


model = DDG #Выбираем модель нейросети
if sys.platform == 'win32':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def voice_settings():
    voice_number = 3 # Измените этот параметр для смены голоса
    return voice_number

def voice_noise():
    noise = 8 # Регулирование уровня окружающего шума (Влияет на скорость и на качество распознования голоса)
    return noise


# Выполнение комманд #
def func(voice_input):
    try:
        #----Анализатор команды----# (Если вы хотите обработать какую-то свою команду пропишите сюда что надо узнать и что вывести)
        response = g4f.ChatCompletion.create(model=g4f.models.gpt_4o_mini,
                                        messages=[{"role": "user", "content": f'проанализируй текст и выведи в ответ только 1 слово, если человек просит узнать погоду выведи pogoda, если человек хочет узнать время выведи time, если в тексте есть слово загуглить выведи google, если человек просит открыть какуюто программу выведи prog, если человек хочет включить или послушать музыку выведи musik, если человек хочет помотреть ютуб выведи youtube, если человек хочет сгенерировать изображение выведи geni, если ничего из списка не найдено выведи ant: {voice_input}'}],
                                        provider=model,
                                        auth=False)
        #----Анализатор команды----#

        #----Выполнение комманды time----#
        if response == 'time':
            import datetime
            '''43469e4fc908c9dbee08db97cd5660b4'''

            current_time = datetime.datetime.now().time()
            a=''
            for i in str(current_time):
                if str(i) == '.':
                    break
                else:
                    a+=str(i)
            print(current_time)
            output = f'Сейчас {a}'
            return output
        #----Выполнение комманды time----#

        #----Выполнение комманды pogoda----#
        if response == 'pogoda':
            response = g4f.ChatCompletion.create(model=g4f.models.gpt_4o_mini,

                                        messages=[{"role": "user", "content": f'проанализируй текст и выведи в ответ только название города: {voice_input}'}],
                                        provider=model,
                                        auth=False)
            import requests
            city = response
            url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=43469e4fc908c9dbee08db97cd5660b4'
            weather_data = requests.get(url).json()
            temperature = round(weather_data['main']['temp'])

            a = 'Сейчас в городе', city, str(temperature), '°C'
            return a       
        #----Выполнение комманды pogoda----#
         
        #----Выполнение комманды google---#    
        elif response == 'google':
            response = g4f.ChatCompletion.create(model=g4f.models.gpt_4o_mini,

                                        messages=[{"role": "user", "content": f'выведи только то что хочет загуглить человек: {voice_input}'}],
                                        provider=model,
                                        auth=True)
            import webbrowser
            a = response.replace(' ', '+')
            url =f'https://www.google.com/search?q={a}'
            webbrowser.open(url, new=0, autoraise=True)
            a = f'Открыла гугл с запросом:  {response}'
            return a
        #----Выполнение комманды google---#  

        #----Выполнение комманды musik---#  
        elif response == 'musik':
            import webbrowser
            url ='https://music.yandex.ru/home'
            a = f'Открываю Яндекс музыка'
            webbrowser.open(url, new=0, autoraise=True)
            return a
        #----Выполнение комманды musik---#

        #----Выполнение комманды youtube---#
        elif response == 'youtube':
            import webbrowser
            a = f'Открываю Youtube'
            url ='https://www.youtube.com/watch?v=wjI_iJyjiU8'
            webbrowser.open(url, new=0, autoraise=True)
            return a
        #----Выполнение комманды youtube---#

        #----Выполнение комманды ant---#
        elif response == 'ant':
            response = g4f.ChatCompletion.create(model=g4f.models.gpt_4o_mini,

                                        messages=[{"role": "user", "content": f'{voice_input}'}],
                                        provider=model,
                                        auth=False)
            print(response)
            a = response.replace('*','')
            return a
        #----Выполнение комманды ant---#
        elif response == 'geni':
            print(1)
            import json
        import time
        import base64
        import requests


        import json
        import time

        import requests


        class Text2ImageAPI:

            def __init__(self, url, api_key, secret_key):
                self.URL = url
                self.AUTH_HEADERS = {
                'X-Key': f'Key {api_key}',
                'X-Secret': f'Secret {secret_key}',
                }

            def get_model(self):
                response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
                data = response.json()
                return data[0]['id']

            def generate(self, prompt, model, images=1, width=1024, height=1024):
                params = {
                "type": "GENERATE",
                "numImages": images,
                "width": width,
                "height": height,
                "generateParams": {
                    "query": f"{prompt}"
                    }
                }

                data = {
                    'model_id': (None, model),
                    'params': (None, json.dumps(params), 'application/json')
                }
                response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
                data = response.json()
                return data['uuid']

            def check_generation(self, request_id, attempts=10, delay=10):
                while attempts > 0:
                    response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
                    data = response.json()
                    if data['status'] == 'DONE':
                        return data['images']

                    attempts -= 1
                    time.sleep(delay)


        response = g4f.ChatCompletion.create(model=g4f.models.gpt_4o_mini,

                                        messages=[{"role": "user", "content": f'выведи только описание картинки которую хочет сгенерировать человек: {voice_input}'}],
                                        provider=model,
                                        auth=True)
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', 'FE17C1CB50A9A0BDEBC9DFC26EADF64B', '1116E70BB5CB0E55E8150E00AEDDA37C')
        model_id = api.get_model()
        uuid = api.generate(f"{response}", model_id)
        images = api.check_generation(uuid)
        image_base64 = images[0]
        image_data = base64.b64decode(image_base64)
        with open("image.jpg", "wb") as file:
                file.write(image_data)
        os.startfile(r'image.jpg')
        a = 'Вот результат!'
        return a

        """
        Если вы вписали свою команду в анализатор, то ваша функция должна выглядеть так:
        а = слово которое должен вывести анализатор на вашу комманду
        elif response == а:
            Ваш код тут...
        
            
        Если ваша команда не требует анализа, то ваша функция выглядит так:
        а = 'то что должен сказать человек для активации вашей функции'
        elif voice_input == а:
            Ваш код тут...
        """


    except:
        a = 'Ошибка запроса!'
        return a