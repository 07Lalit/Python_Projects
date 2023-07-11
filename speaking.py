""" 
                                                 About this program 
                                              *************************

 This is a python weather program using request module will get you the data of the city given by the User to make it more interactive  added gTTS 
 module is a very easy to use tool which converts the text entered, into audio which can be saved as a mp3 file. The gTTS API supports several languages 
 including English, Hindi, Tamil, French, German and many more.The speech can be delivered in any one of the two available audio speeds, fast or slow. 
 and using playsound module play that weather data.
                        


"""

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
            






