import requests
from bs4 import BeautifulSoup
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
from click import command
import speech_recognition as sr
import pyttsx3
import urllib
import pywhatkit
from datetime import datetime
import wikipedia
import wolframalpha
import random
import pyjokes
dictionary = {}
engine = pyttsx3.init()
app_id = 'Y8TXRK-37X64HY7R4'
#song = AudioSegment.from_mp3("C:\\Users\\Yash soni\\Desktop\\chatbot\\Rakh Teri Maa Ka - Hera pheri.mp3")




def reply(text):
    engine.say(text)
    engine.runAndWait()
    


listener = sr.Recognizer()
def run_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            #if 'bixby' in command:
             #   command = command.replace('bixby',' ')
            return command
    except:
        reply('oops! unable to get you!')
        print('unable to get you!')
    
     

greet_inputs = "hi"
greet_outputs = ["Hi","hello","hi, howz it going?","hi, nice to see you again!"]
       
         


def player():
    command = run_command()
    if 'play' in command:
        song = command.replace('play','')
        print('playing ' + song)
        reply('playing' + song)
        pywhatkit.playonyt(song)

    elif "who is " in command:
        person = command.replace('who is ','')
        info = wikipedia.summary(person, 1)
        print(info)
        reply(person + 'is' + info)
    elif "save a number" in command:
        reply('okay! what is the number')
        value = run_command()
        reply('save the number as?')
        key = run_command()
        
        dictionary[key] = value
        reply('okay done!')
        print('number ' + value + 'saved as ' + key)
        reply('number' + value + 'saved as' + key)
        
    elif "message" in command:
        pywhatkit.sendwhatmsg('+19057820827','Hello! I am Jarvis',1,40)
        reply('okay message sent!')
    elif "call" in command:
        command = command.replace('call','')
        print(dictionary[command])
        reply('okay callin' + dictionary[command])   
    elif 'joke' in command:
        reply('sure why not!')
        joker = pyjokes.get_joke()
        print(joker)
        reply(joker)
        
    
    elif "alarm" in command:
        if "alarm" in command:
            reply('Okay! go on...')
            alarmH = int(input('at what hours: '))
            #reply(alarmH + ' Hours and what minutes?')
            alarmM  = int(input('Please enter the minutes: '))
            #reply('AM or PM?')
            ampm = str(input('AM or PM: '))
            reply('okay i am on it!')
            print('alarm set')
            if ampm == "pm":
                alarmH = alarmH + 12
                while True:
                    if(alarmH == datetime.now().hour and alarmM == datetime.now().minute):
                        print('Time to wake up')
                        #take a note when you want to play an mp3 file in python with playsound library
                        #try to add double backshlash in your whole path as done below
                        #otherwise it will throw unicode error!
                        playsound("C:\\Users\\Yash soni\\Desktop\\chatbot\\Rakh Teri Maa Ka - Hera pheri.mp3\\")
                        break
            else:    
                while True:
                    if(alarmH == datetime.now().hour and alarmM == datetime.now().minute):
                        print('Time to wake up')
                        playsound("C:\\Users\\Yash soni\\Desktop\\chatbot\\Rakh Teri Maa Ka - Hera pheri.mp3")
                        break
    #this part is not working
    elif "temperature" in command:
        search = "temprature in toronto"
        url = f"https://www-google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_ = "BNeawe").text
        print("current temprature is " + temp)
    elif "going out" in command:
        question = "temprature"
        client =wolframalpha.Client(app_id)
        res = client.query(question)  
        answer = next(res.results).text
        if answer <= '0':
            print(answer)
            reply("The temprature is " + answer + " please wear a jacket its cold outside!")
        else:
            reply(answer)
            reply("Have a nice day champ!")
                        
        

    elif "search" in command:
        reply('Okay! ask me..')
        question = run_command()
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        reply(answer)
        print(answer)
           


while True:
    command = run_command()
    if 'sara' not in command:
        run_command()
    else:
        if greet_inputs in command:
            reply(random.choice(greet_outputs))
            player()
        
    


    


'''def wolfram():
    print('AI activated....')
    command = run_command()
    question = command
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    reply(answer)
    print(answer)'''




