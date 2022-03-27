import playsound
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
        
    
    elif "alarm" or "timer" in command:
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
                        reply('beep beep')
                        playsound("F:\New folder\Rakh Teri Maa Ka - Hera pheri.mp3")
                        break
            else:    
                while True:
                    if(alarmH == datetime.now().hour and alarmM == datetime.now().minute):
                        print('Time to wake up')
                        reply('beep beep')
                        break        
        elif "timer" in command:
            reply("for what time dear!")
            time = int(input("for how many minutes: "))
            timer = datetime.now().minute + time
            if datetime.now().minute == timer:
                print('time is up buddy!')

            
            '''if "hour" in time:
                time = time.replace('hours','')
                converter = int(time)
                timerH = datetime.now().hour + converter
                while True:
                 if datetime.now().hour == timerH :
                    print("Time's UP!")
            if "minute" in time:
                time = time.replace("minute","")
                converter = int(time)
                timerM = datetime.now().minute + converter
                while True:
                 if datetime.now().minute == timerM :
                    print("Time's UP!")
            elif "seconds" in time:
                time = time.replace('seconds',"")
                converter = int(time)
                timerS = datetime.now().second + converter
                while True:
                 if datetime.now().second == timerS :
                    print("Time's UP!") '''
            

            

        
#have a look on this else statement please!
    else:
        if 'bye' in command:
            reply('see ya, have a great one')

        elif command not in ' ' :
            client = wolframalpha.Client(app_id)
            res = client.query(command)
            answer = next(res.results).text
            reply(answer)
            print(answer)
        else:
            reply('Is there anything else i can help you?') 
            player()   


while True:
    command = run_command()
    if 'sara' in command:
        if greet_inputs in command:
            reply(random.choice(greet_outputs))
            player()
        else:
            run_command()    
    


    


'''def wolfram():
    print('AI activated....')
    command = run_command()
    question = command
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    reply(answer)
    print(answer)'''




