import speech_recognition as sr
import webbrowser
import pyttsx3
import songlibrary
import  requests
 #speech recognition functionality deti h

def speak(text):
    engine = pyttsx3.init() 
    engine.say(text)
    engine.runAndWait()

newsapi = "78fb0a269bd7408ab69221679ef307d5"

def processCommand(command):
    if "open youtube" in command.lower():
        print("Opening Youtube")
        speak("Opening Youtube")
        webbrowser.open("www.youtube.com")
    elif"open instagram" in command.lower():
        print("Opening Instagram")
        speak("Opening Instagram")
        webbrowser.open("www.instagram.com")
    elif "open google " in command.lower():
        print("Opening google")
        speak("Opening google")
        webbrowser.open("www.google.com")
    elif "open my github" in command.lower():
        print("Opening github")
        speak("Opening github")
        webbrowser.open("https://github.com/")
    elif  command.lower().startswith("play"):
        print(command.lower())
        song = command.lower().split(" ")[1]
        link = songlibrary.music[song]
        webbrowser.open(link)
    elif  "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                print(article['title'])
                speak(article['title'])




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

                if "terminate" in command.lower():
                    print("Thankyou sir , program terminated")
                    speak("Thankyou sir .Program Terminated")
                    break

                processCommand(command)
              
        
    except Exception as e:
        print(e)