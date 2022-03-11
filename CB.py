from click import command
import speech_recognition as sr
import pyttsx3
import urllib
import pywhatkit
import datetime
import wikipedia
import wolframalpha
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
            #if 'bixby' in command:
             #   command = command.replace('bixby',' ')
    except:
        print('unable to get you!')
    return command

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
    else:
        client = wolframalpha.Client(app_id)
        res = client.query(command)
        answer = next(res.results).text
        reply(answer)
        print(answer)

starter = run_command()

while 'bixby' not in starter:
       run_command()
else:
    reply('Hi! how can i help you today?')
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




