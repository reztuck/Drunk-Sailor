#Created by Tucker
#2016
#https://www.linkedin.com/in/tuckerlogan
#https://www.github.com/reztuck

import os
import time
checker =("N")

#Takes input from user and applies it to story

while checker == ("N"):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
"""
  __      ____     _   _   _     _   _   _ 
|  _ \   |  __ \  | | | | |  \  | | | | / / 
| | \ \  | |__| | | | | | | \ \ | | | |/ / 
| |  | | |  _  /  | | | | | |\ \| | | _ | 
| |_/ /  | | \ \  | |_| | | | \ \ | | |\ \ 
|___ /   |_|  \_\ |_____| |_|  \__| |_| \_\ 
 _____     ___     _         ___     ____ 
|  ___|   / _ \   | |      / ___ \  |  __ \ 
| |___   / /_\ \  | |     | |   | | | |__| | 
|___  | |  ___  | | |     | |   | | |  _  / 
 ___| | | |   | | | |___  | |___| | | | \ \  
|_____| |_|   |_| |_____|  \_____/  |_|  \_\ 
 ___	     ______ 
/_  | 	    |  __  | 
  | |	    | |  | | 
  | |       | |  | | 
 _| |_   _  | |__| | 
|_____| |_| |______| 

Make sure that the application is ran from CMD

* Made by Tucker
* github.com/reztuck
* 2016

The program will start automatically within 10 seconds
""")
    time.sleep(7)
    print("\n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input("Your name:  ")
    name = str.capitalize(name)
    gender = input("Male/Female:  ")
    gender = str.capitalize(gender)
    heOrShe = ("")
    
    # Uses input of gender to also apply he/she to the story
    if gender == "F":
        gender = "Female"
    if gender == "M":
        gender = "Male"

    if gender == "Female":
        heOrShe = "she"
    elif gender == "Male":
        heOrShe = "he"

    heOrShe = str.capitalize(heOrShe)
    gender = str.lower(gender)

    list = [name, gender, heOrShe]
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("# Character Info")
    print ("Gender:     " + str.capitalize(gender))
    print ("Name:       " + str.capitalize(name))
    checker = input("\n\nData correct? Y/N\n")
    checker = str.upper(checker)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if checker == "NO":
        checker = "N"
    
    if checker == "YES":
        checker = "Y"

    if checker == "Y":

        os.system('cls' if os.name == 'nt' else 'clear')
        print ("\nPlease wait... currently utilizing Google's deep neural network, machine\n learning, super-computer to process my insanely complex algorithm\n\n")
    


        time.sleep(5)
        print ("$.&Dosomestuff (*$)\\warmup_flux_capacitor: !launch+ Bunch of useless text")
        time.sleep(.8)
        print ("%InitiateCode:Sectore_booga:$More cool useless text")
        time.sleep(.8)
        print ("%.$Stuff_no_one_knows.* (Initiate beep beep and boop)")
        time.sleep(.8)
        print ("Some thinking dots ..............\n\n")
        time.sleep(5)
        print ("Beep Beep and boop... (followed by useless dial-up tones) and we are DONE!\n\n")
        time.sleep(4)
        print ("I will now attempt to load the data... if you do not have 72 terabytes\n of available HDD space your computer will explode immediatly")
        
        time.sleep(4)
        print("\n\n\n3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("...")
        time.sleep(2)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        intro = ("# {0}'s story of drunk-sailor glory...\n\n".format(*list))
        print (intro)


        story = (
"""    {0} was a {1}
    who really liked to sail
    {2} drunk a lot of ale 
    but went very pale

    {2} was rushed away 
    but was forced to stay
    {0} went home in a week 
    but was still a bit of a freak!\n\n\n\nFor the record I am not a drunk... but apparently you are! :p\n\nCheers!\n\nTucker\n\nhttps://www.linkedin.com/in/tuckerlogan\n""".format(*list))
    
        print (story)
        restartProgram = input("Restart program? (Y/N)")
        restartProgram = str.upper(restartProgram)
        if restartProgram == "NO":
            restartProgram = "N"
    
        if restartProgram == "YES":
            restartProgram = "Y"

        if restartProgram == ("Y"):
            checker = ("N")
        else: 
            exit()
        
