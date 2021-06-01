'' '
    Descripción:
    Crea tu propio asistente virtual con python.
    Autor: AlejandroV
    Versión: 1.0
    Video: https://youtu.be/8WKjX0dbh4E
'' '
from os import replace
import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia
from wikipedia.wikipedia import summary
import pyjokes
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr

name = '-name-'

key = 'YOUR_API_KEY_HERE'

flag = 1 

listener = sr.Recognizer()

engine = pyttsx3.init()

r = sr.Recognizer()

mic = sr.Microphone()

sr.Microphone.list_microphone_names()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando..")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()

            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                talk("Vuelve a intentarlo, no reconozco: " + rec)
    except:
        pass
    return rec 

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo '+music)
        pywhatkit.playonyt(music)
    elif 'cuantos suscriptores tiene' in rec:    
        subs = rec.replace('cuantos suscriptores tiene', '').strip()
        data = urllib.request.urlopen(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={name_subs.strip()}&key={key}').read()
        subs = json.loads(data)["items"][0]["statistics"]["subscribeCount"]
        talk(name_subs + " tiene {:,d}".format(int(subs)) + " suscriptores!")
    elif 'hora' in rec:
        hora = datetime.datetime().now().strftime('%I:%M %p')
        talk("Sona las "+hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        info = wikipedia.summary(order, 1)
        talk(info)   
    elif 'exit' in rec:
        flag = 0
        talk("Saliendo...")
    elif 'chiste' in rec:
        chiste = pyjokes.get_joke("es")
        talk(chiste)
    else:
        talk("Vuelve a intentarlo, no reconozco: " + rec)
    return flag

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                               client_secret="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

while flag:
    flag = listen() 
