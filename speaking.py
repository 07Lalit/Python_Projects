from gtts import gTTS
import playsound as py
import requests

if __name__ == '__main__' :
    cnt=1
    print("\t\t\tWelcome to RoboSpeaker 1.1. Created by Lalit")
    
    language = 'gu'
    while True:
        city =  input("Enter name of the city (type q or Q to stop) : \n")
        cnt= cnt+1
        
        if city in set("qQ"):
            myText="Thank You"
            output = gTTS(text=myText, lang=language)
            output.save(f"output{cnt}.mp3")
            py.playsound(f"output{cnt}.mp3")
            break

        else:
            url= f"http://api.weatherapi.com/v1/current.json?key=c77b695eb4024a6cafd115358231007&q={city}"

            r= requests.get(url)
            out = r.text
            
            print(out)
            
            output =gTTS(text=out,lang=language)
            output.save(f"output{cnt}.mp3")
            py.playsound(f"output{cnt}.mp3")
            continue
            






