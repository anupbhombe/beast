import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
# import google.generativeai as genai
import os

recognizer=sr.Recognizer()
engine=pyttsx3.init()
# newsapi= "paste news api here from news api"

def speak(text):
    engine.say(text)
    engine.runAndWait()

#i have used gemini ai here because open ai is paid try to run it also
# def aiprocess(command):
#     client=genai.configure(api_key=os.environ["AIzaSyCW4W9VuJ0gNYa03Aj2v4NMohuXqF9h4Jo"])

#     model = genai.GenerativeModel('gemini-1.5-flash')

#     response = model.generate_content(command)
#     print(response.text)

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in command.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    else:
        speak("sorry")


    # elif "news" in c.lower():
    #     r=requests.get("news api key")
    #     if r.status_code==200:
    #         data=r.json()
    #         articles=data.get("articles",[])
    #         for article in articles:
    #             speak(article["title"])

    # else:
    #     #let open ai handle the request
    #     output=aiprocess(command)
    #     speak(output)


if __name__=="__main__":
    speak("hey, I am beast how may I help you")

    while True:
        #listen for the wake word 
        #obtain audio from the microphone

        r=sr.Recognizer()


        print("recognizing....")

        #recognize speedch using google
        try:
            with sr.Microphone() as source:
                print("How may I help you...")
                audio=r.listen(source, timeout=4, phrase_time_limit=4)
            word=r.recognize_google(audio)
            if(word.lower()== "beast"):
                speak("Yes")
                #listen for command
                with sr.Microphone() as source:
                    print("Beast active...")
                    audio=r.listen(source, timeout=4, phrase_time_limit=4)
                    speak(source)
                    command=r.recognize_google(audio)

                    processCommand(command)


            # print("Sphinx thinks you said "+r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Beast could not understand audio")
        except Exception as e:
            print("error;{0}".format(e))