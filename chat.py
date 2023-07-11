""" 
                           #  About this Program #
                           ==========================

This is a python program named as 'Text-to-speak' converter using gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with 
Google Translate text-to-speech API. gTTS is a very easy to use tool which converts the text entered, into audio which can be saved as a mp3 file. 
The gTTS API supports several languages includingEnglish, Hindi, Tamil, French, German and many more. The speech can be delivered in any one of the
two available audio speeds, fast or slow.and playsound module to play that mp3 file .


"""




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
            






