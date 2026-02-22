import speech_recognition as sr
import webbrowser
import pyttsx3 

 #speech recognition functionality deti h

def speak(text):
    engine = pyttsx3.init() 
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    if( command.lower()== "open youtube"):
        print("Opening Youtube")
        speak("Opening Youtube")
        webbrowser.open("www.youtube.com")
    elif( command.lower()== "instagram"):
        print("Opening Instagram")
        speak("Opening Instagram")
        webbrowser.open("www.instagram.com")

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    # Listen for walk of jarvis
while True:    
    r = sr.Recognizer()
      # recognize speech using google
    print("recognizing...")
    try: 
        #walkup call
        with sr.Microphone() as source :
            print("Listening...")
            audio = r.listen(source)
        
        word = r.recognize_google(audio)
        if(word.lower()== "jarvis"):
            print(word)
            
            # starting listening for commands
            with sr.Microphone() as source:
                print("Jarvis active...")
                print("yes sir ")
                speak("yes sir ")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print("you :",command)
                processCommand(command)
        elif(word.lower()== "jarvis terminate"):
            print("Thankyou sir , program terminated")
            speak("Thankyou sir .Program Terminated")
            break
        
    except Exception as e:
        print(e)