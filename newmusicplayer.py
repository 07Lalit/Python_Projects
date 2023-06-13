from playsound import playsound


print("\t\t\t\t\tMUSIC PLAYER ",chr(127925),chr(128251) )
print("\n")

s = input("Do you want to listen the songs..!(0/1) : " )


if(s== "1"):
			print("\t\t\tLIST OF SONGS ",chr(127911),chr(128466),chr(129311))
			print(" 1) Humare Sath shree Raghunath", chr(127752))
			print(" 2) Despacito ", chr(128147))
			print(" 3) Chala jata hu ", chr(128153))
			print(" 4) Dil Nu ", chr(128150))
			print(" 5) Jadugar ", chr(127754))
			print(" 6) Andhadhun Title track ", chr(127755))
			print("\n")
			i = input("Enter the no of the song you want to play : ")
			if(i=="6"):
				playsound("C:\\music\Andhadhun Title Track Raftaar 128 Kbps.mp3")
			elif(i=="2"):

				playsound("‪C:\\music\\Despacito(PagalWorld.com.se).mp3")
			elif(i=="3"):
				playsound("C:\\music\\Chala Jata Hoon - Sanam (Band) 320 Kbps.mp3‪‪‪")
			elif(i=="4"):
				playsound("‪C:\\music\\Dil-Nu.mp3")
			elif(i=="5"):
				playsound("C:\\music\\Jadugar Aisa Jadu Kar - Lofi - Paradox ! Hindi.mp3")
			elif(i=="1"):
				playsound("‪C:\\music\\Despacito(PagalWorld.com.se).mp3")
			elif s != set("123456"):
				print("No such songs in the Playlist .try again..!",chr(128535))


else:
	print("Thank You",chr(128512))