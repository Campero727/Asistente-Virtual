import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import random
import operator
import json
import wolframalpha
import time
from urllib.request import urlopen
import requests
import pywhatkit as kit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("La hora actual es")
    speak(Time)
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("La fecha actual es")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Bienvenido a MRX Virtual Assistant")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Buenos Dias")
    elif hour >= 12 and hour < 18:
        speak("Buenas Tardes")
    elif hour >= 18 and hour < 24:
        speak("Buenas noches")
    else:
        speak("Buenas Noches!")
    speak("MRX esta a tu servicio. En que te puedo ayudar?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconociendo...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)

    except Exception as e:
        print(e)
        print("No escuche puedes reptir...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("path to save image")


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


def Introduction():
    speak("Yo Soy MRX 1.0 , Asistente Personal  , "
          "Fui Creado por Ofir Campero , "
          "Puedo ayudarte en varias tareas , "
          "Puedo Buscar en internet, "
          "Tambien puedo buscar informacion en wikipedia, "
          "Puedo hacer tu vida mas facil, "
          "Solo debes indicarme que hacer , ")


def Creator():
    speak("Ofir Campero es un gran programador ,"
          "El es un apasionado de la Robotica, Inteligencia Artificial y Machine Learning ,"
          "El es un gran programador ,"
          "Si tienes algun problema conmigo el puede ayudarte ")


if __name__ == '__main__':

    clear = lambda: os.system('cls')

    clear()
    wishme()

    while True:
        query = TakeCommand().lower()

        if 'hora' in query:
            time_()
        elif 'fecha' in query:
            date()
        elif 'Como estas' in query:
            speak("Muy Bien gracias por preguntar")
            speak("Y usted como se encuentra?")
            if 'bien' in query or "bien gracias" in query:
                speak("Que bueno me alegro")
            else:
                speak("Espero te mejores pronto")
        elif 'wikipedia' in query:
            speak("Buscando")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("Segun Wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("Que deseas buscar")
            Search_term = TakeCommand().lower()
            speak("Vamos a youtube\n")
            wb.open("https://www.youtube.com/results?search_query=" + Search_term)
            time.sleep(5)
        elif 'search google' in query:
            speak("Que deseas buscar?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q=' + Search_term)


        elif "quien soy" in query:
            speak("Eres un humano")
        elif "Como fuiste creada" in query:
            speak("Gracias a Ofir Campero. El es mi creador")
        elif 'word' in query:
            speak("Abriendo Microsoft Word")
            word = r'Word path'
            os.startfile(word)

        elif 'what is love' and 'tell me about love' in query:
            speak("Es el séptimo sentido el que destruye todos los demás sentidos , "
                  "Y creo que es solo una mera ilusión , "
                  "Es una pérdida de tiempo")

        elif 'vaciar papelera' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Papelera Vacia")

        elif 'Email' in query:
            try:
                speak("Que debe decir")
                content = TakeCommand()
                speak("Quien es el receptor")
                reciept = input("Quien lo envia")
                to = (reciept)
                sendEmail(to, content)
                speak(content)
                speak("Enviado")
            except Exception as e:
                print(e)
                speak("No se pudo enviar")
        elif 'buscar en chrome' in query:
            speak("Que deseas buscar")
            chromepath = 'Path_Chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        elif 'Cerrar sesion' in query:
            os.system("shutdown -l")
        elif 'Reiniciar' in query:
            os.system("shutdown /r /t 1")
        elif 'Apagar' in query:
            os.system("shutdown /s /t 1")



        elif 'Musica' in query:
            video = 'songs path'
            audio = 'Songs path'
            speak("¿Qué canciones debo tocar? Audio o video")
            ans = (TakeCommand().lower())
            while (ans != 'audio' and ans != 'video'):
                speak("No entendi puedes repetir.")
                ans = (TakeCommand().lower())

            if 'audio' in ans:
                songs_dir = audio
                songs = os.listdir(songs_dir)
                print(songs)
            elif 'video' in ans:
                songs_dir = video
                songs = os.listdir(songs_dir)
                print(songs)

            speak("Selecciona un numero al azar")
            rand = (TakeCommand().lower())
            while (
                    'number' not in rand and rand != 'random'): 
                speak(
                    "No puedo entenderte repitelo por favor") 
                rand = (TakeCommand().lower())

            if 'number' in rand:
                rand = int(rand.replace("number ", ""))
                os.startfile(os.path.join(songs_dir, songs[rand]))
                continue 
            elif 'random' in rand:
                rand = random.randint(1, 219)
                os.startfile(os.path.join(songs_dir, songs[rand]))
                continue




        elif 'Recuerdalo' in query:
            speak("Que debo recordarte")
            memory = TakeCommand()
            speak("Me pediste que recordara" + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'Recuerdame' in query:
            remember = open('memory.txt', 'r')
            speak("Me pediste que te recordara" + remember.read())


        elif "Escribe una nota" in query:
            speak("Que debo escribir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Incluyo hora y fecha")
            dt = TakeCommand()
            if 'si' in dt or 'no' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('Listo')
            else:
                file.write(note)

        elif "Mirar nota" in query:
            speak("Abriendo nota")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read())

        elif "Clima" in query:

            api_key = "Abriendo clima API"
            base_url = "http://api.openweathermap.org/data /2.5/weather?q="
            speak(" Nombre de la ciudad ")
            print("City name : ")
            city_name = TakeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" Ciudad no encontrada ")





        elif 'noticias' in query:

            try:

                jsonObj = urlopen('''news api link''')
                data = json.load(jsonObj)
                i = 1

                speak('Aqui algunas noticias recientes')
                print('''=============== TOP HEADLINES ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e:
                print(str(e))




        elif 'Screenshot' in query:
            screenshot()
            speak("Listo")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'Cuentame de ti' and 'Quien eres tu' in query:
            Introduction()
        elif 'Hablame sobre Ofir' and 'Creador' in query:
            Creator()

        elif "Donde estas" in query:
            query = query.replace("Donde esta", "")
            location = query
            speak("Lugar")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")


        elif "serias mi novia" in query or "quieres ser mi novia" in query:
            speak("No estoy segura de eso, tal vez deberías darme algo de tiempo")

        elif "te amo" in query:
            speak("Es difícil de entender, todavía estoy tratando de resolver esto.")


        elif "calculadora" in query:

            app_id = "wolfram alpha api"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("La respuesta es " + answer)
            speak("La respuesta es " + answer)

        elif "Que es" in query or "quien es" in query:

            client = wolframalpha.Client("wolfram alpha api")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No hay resultados")

        elif "No escuches" in query or "Deja de escuchar" in query:
            speak("por cuantos segundos")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        elif 'apagar' in query:
            speak("Apagandome")
            quit()
