import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia


listener = sr.Recognizer()

engine = pyttsx3.init()

with sr.Microphone() as source:
    try:
        print("Habla ahora")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
        if 'larry' in command:
            command = command.replace('larry', '')
            if 'play' in command:
                command = command.replace('play', '')
                engine.say((f'you said {command}'))
                engine.runAndWait()
                pywhatkit.playonyt(command)
            if 'wiki' in command:
                command = command.replace('wiki', '')
                result = wikipedia.summary(command, 1)
                engine.say(result)
                engine.runAndWait()

    except Exception as err:
        print(err)
