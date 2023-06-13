from playsound import playsound 

print("\t\t\t\t\tMUSIC PLAYER ",chr(127925),chr(128251) )
print("\n")

s = int(input("Do you want to listen the songs..!(0/1) : " )


if(s>0):
			print("\t\t\tLIST OF SONGS ",chr(127911),chr(128466),chr(129311))
			print(" 1) Zara Zara instrumental ", chr(127752))
			print(" 2) Zara Zara instrumental ", chr(128147))
			print(" 3) Zara Zara instrumental ", chr(128153))
			print(" 4) Zara Zara instrumental ", chr(128150))
			print(" 5) Zara Zara instrumental ", chr(127754))
			print(" 6) Zara Zara instrumental ", chr(127755))
			print("\n")
			i = int("Enter the no of the song you want to play : ")
				if(i==1):
					playsound("C:\\music\\Zara_Zara_Instrumental-Ringtonestar.Net.mp3")
				elif(i==2):
					playsound("‪‪‪C:\\music\\Andhadhun Title Track Raftaar 128 Kbps.mp3")	
				elif(i==3):
					playsound("C:\\music\\Chala Jata Hoon - Sanam (Band) 320 Kbps.mp3‪‪‪")
				elif(i==4):
					playsound("‪‪‪‪C:\\music\\English songs bgm.mp3")
				elif(i==5):
					playsound("‪‪‪C:\\music\\Jadugar Aisa Jadu Kar - Lofi - Paradox ! 												Hindi.mp3")			
				elif(i==6):
					playsound("‪‪‪‪C:\music\Dil-Nu.mp3")
elif:
	print("No such songs in the Playlist .try again..!",chr(128535))


else:
	print("Thank You",chr(128512))