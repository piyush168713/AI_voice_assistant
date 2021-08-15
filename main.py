import pyttsx3
import speech_recognition as sr

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again master")
            return "None"
  
    return Query
    

def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


# Driver Code
if __name__ == '__main__':
   
    while True:
        command = take_commands()
        if "exit" in command:
            Speak("Sure master! as your wish")
            break
        if "What is your name" in command:
            Speak("Hello master, my name is Jarvis")
        if "Are you a bot?" in command:
            Speak("I am an automated ai machine made by miss Aindrila.I act based on your command. I am a quick learner.")
        if "How are you feeling today?" in command:
            Speak("I am happy as a happy Jarvis")
