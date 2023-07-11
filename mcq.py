""" 
                           #  About this Program #
                           ==========================

This is a console based Quiz Program using various concepts of python programming and several  
modules like time and playsound to make it more interactive and user friendly .

"""
import playsound as pt
import time
print("\t\t\t\t\t\t",chr(128329))
name = str(input("Enter Your Full Name : "))
time.sleep(2)
rollno = str(input("Enter your Enrollment no. : "))
Sum =0
time.sleep(2)
ask = str(input("If You want to Start the exam { print : Y(in_upper_case)and N (in_upper_case) } "))

if (ask=='Y'):
    time.sleep(3)
    print("choose the correct option  " ,chr(128417))
    print("*****************************************")
    print("  ")
    time.sleep(3)
    print("Q1) who is the develper of Python ?")
    print("1) Guido van Rosum \n 2) james Gosling2)\n 3)charles babbage \n 4)Bjarne Strousstroup")
    a=int(input("Enter the correct option (1,2,3,4) : "))
    if (a==1):
        Sum=Sum+1
        
    print("\n ")
    time.sleep(3)
    print("Q2) How is a code block indicated in Python?")
    print("1) Bracket \n 2)key \n 3)Indentation 4)None of the above.")
    b=int(input("Enter the correct option (1,2,3,4) : "))
    if (b==3):
        Sum=Sum+1
    
    print("\n ")
    time.sleep(3)
    print("Q3) Which of the following concepts is not a part of Python?")
    print("1) Pointer \n 2) Loop \n 3) dynamic type \n 4)All the above.")
    c=int(input("Enter the correct option (1,2,3,4) : "))
    if (c==1):
        Sum=Sum+1
        
        
    print("\n ")
    time.sleep(3)
     
    print("Q4) Is Python case sensitive when dealing with identifiers?")
    print("1) yes \n 2) no \n 3) dynamic type \n 4)None of these.")
    d=int(input("Enter the correct option (1,2,3,4) : "))
    if (d==1):
        Sum=Sum+1
        
    print("\n ")
    time.sleep(3)
    
    print("Q5) Which of the following is the correct extension of the Python file?")
    print("1) .java \n 2) .py \n 3) .c\n 4).pl")
    e=int(input("Enter the correct option (1,2,3,4) : "))
    if (e==2):
        Sum=Sum+1  
        
    print("***************************************************************") 
    time.sleep(2)
    print("\t\tprocessing result please wait..........")
    time.sleep(4)
if (ask=='Y'):
    print("  ")   
    print("Result",chr(128515)) 
    print("\t\tName = ", name , end ='\t\t\t\t')
    print("Enrollment no = ", rollno )
    print("\t\tMarks out of 5 =", Sum , end ='\t\t\t\t')
    print("percentage = ", (Sum/5)*100 ,"%" ) 
    
elif ask=='N':
    print("Thank You",chr(128512))

if Sum>=4 :
    print("Hurray you're outstanding..", chr(127881),chr(127942))
    print("Thank You...!", chr(128512))
    pt.playsound("C:\\music\\English songs bgm.mp3")

else:
    print("Try Again....",chr(128521))

   


if (ask=='N'):   
    print("khatam tata good byee",chr(128053),chr(128079))
    
