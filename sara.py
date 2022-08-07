#imported libraries needed to operate the different functions added in the assistant
import json
import pickle
import sys
#from typing_extensions import Self
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
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from saraui import Ui_SaraGui
dictionary = {}
pickle_out = open("data.py","wb")
pickle_in = open("data.py","rb")
engine = pyttsx3.init()
app_id = 'Y8TXRK-37X64HY7R4'




#creating a filename variable for the feature of storing notes! this variable has json file connected.
filename = "./data/notesdata.json"
# a json database file for adding numbers to database.
numfile = "./data/numbers.json"
#A function for reading the data in the json file.
def view_data():
    
    with open(filename, 'r') as f:
        temp = json.load(f)
        for entry in temp:
            print(entry)

#creating a function to add data to your database
def add_data(notes):
    item_data = {}
    with open(filename, "r") as f:
        temp = json.load(f)
        item_data["notes"] = notes
        temp.append(item_data)
        with open(filename, 'w') as f:
            json.dump(temp, f)

#creating a function to add phone numbers to a different database

def add_number(value):
            add_num = {}
            with open(numfile, 'r') as x:
                tempo = json.load(x)
                reply('Save the number as?')
                name = run_command()
                add_num[name] = value
                tempo.append(add_num)
                with open (numfile, 'w') as y:
                    json.dump(tempo, y)
                reply("okay your number is saved")
                


def reply(text):
    engine.say(text)
    engine.runAndWait()
    


#listener = sr.Recognizer()
#creating a qthread class


def run_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        reply('oops! unable to get you!')
        print('unable to get you!')
    
     

greet_inputs = "hi"
greet_outputs = ["Hi","hello","hi, howz it going?","hi, nice to see you again!"]
   
         


def player(self):
    command = run_command()
#this feature will play videos on youtube
    if 'play' in command:
        song = command.replace('play','')
        print('playing ' + song)
        reply('playing' + song)
        pywhatkit.playonyt(song)
#this feature lets you add notes for daily grocery stuff
    elif "add" in command:
        notes = command.replace("add", ' ')
        add_data(notes)
        reply("Okay its added")
        view_data()
#a feature to connect wikipedia
    elif "who is " in command:
        person = command.replace('who is ','')
        info = wikipedia.summary(person, 1)
        print(info)
        reply(person + 'is' + info)
#saves a number to json database, function for which is created above.
    elif "save a number" in command:
        reply('okay! what is the number')
        value = run_command()
        add_number()
#whatsapp messaging feature, only thing to consider is you will have to use whatsapp web        
    elif "message" in command:
        pywhatkit.sendwhatmsg('+19057820827','Hello! I am Jarvis',1,40)
        reply('okay message sent!')

#recreate the function using json database method
    elif "call" in command:
        command = command.replace('call','')
        #call = str(command)
        d_dictionary = pickle.load(pickle_in)
        
        print(d_dictionary)
        #reply('okay callin' + dictionary[call])   
#feature created with pyjokes, for just programming jokes.
    elif 'joke' in command:
        reply('sure why not!')
        joker = pyjokes.get_joke()
        print(joker)
        reply(joker)
        
#alarm and timer system created just for you on your speaking commands    
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
                        reply("Time's up for whatever you are doing!")
                        break
            else:    
                while True:
                    if(alarmH == datetime.now().hour and alarmM == datetime.now().minute):
                        print('Time to wake up')
                        reply("Time's up for whatever you are doing!")
                        break
#this feature not only tells you what the weather is but also gives you the grocery list to bring while you go out.    
    elif "going out" in command:
        question = "temprature"
        client =wolframalpha.Client(app_id)
        res = client.query(question)  
        answer = next(res.results).text
        if answer <= '0':
            print(answer)
            reply("The temprature is " + answer + " please wear a jacket its cold outside!")
            view_data()
        else:
            view_data()
            reply(answer)
            reply("Have a nice day champ!")
                        
        

        '''elif "search" in command:
            reply('Okay! ask me..')
            question = run_command()
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            reply(answer)
            print(answer)'''

    else: 
        #this commands needs to be organised properly
        if command == '':
            reply("unable to get you!")
        else:
        #this else statement contains wolframalpha's API for everything else you need ;)
            question = run_command()
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            reply(answer)
            print(answer)


          

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.continuous_run()

    def continuous_run(self):
        while True:
            command = run_command()
            if 'sara' not in command:
                run_command()
            else:
                if greet_inputs in command:
                    reply(random.choice(greet_outputs))
                    player(self)

startexecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SaraGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Pictures/Sara images/QmVacftCGVBnPJ5PzZR1b9aBJVAqi93bcGadxKP37CLVv1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startexecution.start()



app = QApplication(sys.argv)
sara = Main()
sara.show()
exit(app.exec_()) 
        

        

       
    


    





