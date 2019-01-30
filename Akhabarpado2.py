import  speech_recognition as sr
import requests
import json
import  time
from win32com.client import Dispatch
import pyaudio
speak=Dispatch("SAPI.spvoice")
def speak_news(str,cnt):
    speak.Speak(f"Speaking news number {cnt}")
    speak.Speak(str)
    time.sleep(1)
data=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f3879b0a82774e5fa704fe52182a7b32")
k=data.text
r1=json.loads(k)
r=sr.Recognizer()
k=0
with sr.Microphone() as src:
    speak.Speak("Hi,this is Alex, tell me how many news you want to listen")
    audio=r.listen(src)
    while True:
        try:
            text=r.recognize_google(audio)
            k=int(text)
            break
        except:
            speak.Speak("Sorry did not recognize ")
cnt=1
for item in r1['articles']:
    if k<=0:
        break
    speak_news(item['title'],cnt)
    cnt+=1
    k-=1
speak.Speak("The new headlines are ended.Thanks for Listening.Come again for more updated news")