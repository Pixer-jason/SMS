import pyautogui as pxr
import time
import os
from BeemAfrica import Authorize, OTP, SMS, AirTime

########################################################################################
print("""\033[1;32;40m
    
        ███╗   ███╗██╗   ██╗███████╗███╗   ███╗███████╗
        ████╗ ████║╚██╗ ██╔╝██╔════╝████╗ ████║██╔════╝
        ██╔████╔██║ ╚████╔╝ ███████╗██╔████╔██║███████╗
        ██║╚██╔╝██║  ╚██╔╝  ╚════██║██║╚██╔╝██║╚════██║
        ██║ ╚═╝ ██║   ██║   ███████║██║ ╚═╝ ██║███████║
        ╚═╝     ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════
    """)
print("\033[1;33;40m \t\tDeveloped By Pixer Jason\n Inspired By TripleHat")
print("\033[1;31;40m Choose options:")
print("\033[1;32;40m########################################\n")
print("1.Send Info SMS\n")
print("2.Send Whatsapp Spam Message\n")
print("3.Git Hub Repository\n")
print("##########################################\n")
ingiza = input("\033[1;37;40mEnter number: ")

os.system('clear')
###########################################################################################



###########################################################################################
if ingiza == '1':
    api_key = input("Enter Your Api key or press enter to use a saved one: ")
    sec_key = input("Enter Your Secret Key or press entter to use a saved one: ")
    mydata = open('data.txt', 'w')
    mydata.write("API KEY = " + api_key + "\n")
    mydata.write("SECRET KEY = " + sec_key + "\n")
    mydata.close()
    os.system('clear')

    msg = input("Enter Your Message: ")
    no = input("Enter Victim No(Begin With country Code Without +): ")
    thb = Authorize(api_key,sec_key)

    tuma = SMS.send_sms(msg,no)

    print(tuma)
 ##########################################################################################


###########################################################################################

elif ingiza == '2':
   print("""\033[1;34;40m

▄▄▌ ▐ ▄▌ ▄ .▄ ▄▄▄· ▄▄▄▄▄.▄▄ ·  ▄▄▄·  ▄▄▄· ▄▄▄·    .▄▄ · ▄▄▄ . ▐ ▄ ·▄▄▄▄  ▄▄▄ .▄▄▄  
██· █▌▐███▪▐█▐█ ▀█ •██  ▐█ ▀. ▐█ ▀█ ▐█ ▄█▐█ ▄█    ▐█ ▀. ▀▄.▀·•█▌▐███▪ ██ ▀▄.▀·▀▄ █·
██▪▐█▐▐▌██▀▐█▄█▀▀█  ▐█.▪▄▀▀▀█▄▄█▀▀█  ██▀· ██▀·    ▄▀▀▀█▄▐▀▀▪▄▐█▐▐▌▐█· ▐█▌▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌██▌▐▀▐█ ▪▐▌ ▐█▌·▐█▄▪▐█▐█ ▪▐▌▐█▪·•▐█▪·•    ▐█▄▪▐█▐█▄▄▌██▐█▌██. ██ ▐█▄▄▌▐█•█▌
 ▀▀▀▀ ▀▪▀▀▀ · ▀  ▀  ▀▀▀  ▀▀▀▀  ▀  ▀ .▀   .▀        ▀▀▀▀  ▀▀▀ ▀▀ █▪▀▀▀▀▀•  ▀▀▀ .▀  ▀
   
   """)

   limit = input("\033[1;37;40mEnter amount of sms: ")
   msg = input("Enter your message: ")
   i=0

   time.sleep(3)
   while i<int(limit):
    pxr.typewrite(msg)
    pxr.press("enter")

    i+=1
############################################################################################

