from gtts import gTTS
import playsound as py

if __name__ == '__main__' :
    cnt=1
    print("\t\t\tWelcome to RoboSpeaker 1.1. Created by Lalit\n")
    
    language = 'en'
    while True:
        myText =  input("Enter What you want me to speak(type q or Q to stop) : \n")
        cnt= cnt+1
        
        if myText in set("qQ"):
            myText="Bye Bye Lalit see you soon.."
            output = gTTS(text=myText, lang=language)
            output.save(f"output{cnt}.mp3")
            py.playsound(f"output{cnt}.mp3")
            break

        else:
            
            output =gTTS(text=myText,lang=language)
            output.save(f"output{cnt}.mp3")
            py.playsound(f"output{cnt}.mp3")
            continue
            






