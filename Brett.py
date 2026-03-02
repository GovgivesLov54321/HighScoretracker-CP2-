#BG 1st code for high score tracker
from Parker_stuff import *
from Lizards_helper_funcs import *
import hashlib

def what():
    with open("HighScoretracker-CP2-\\hi_file.csv", newline='\n') as file:
        fieldnames = ["username", "password"]
        reader = json.reader(file)
#funtion to welcome user as "welcome"
def welcome():
    while True:
        #display welcome to the highscore tracker
        print("Welcome to the highscore tracker")
        #enter a number 1 to check if you have an account 2 to login 3 to create an account 4 to exit program
        print("1 to check if you have an account\n2 to login\n3 to create an account\n to exit program\n")
        user_in = input("What do you want to do")
        #if user entered 1
        if user_in == "1":
            #call enter()
            check_account()
        #if user entered 2
        elif user_in == "2":
            #call login function
            login()
        #if user entered 3
        elif user_in == "3":
            #call create funtion
            create()
        #if user entered 4
        elif user_in == "":
            #exit/break program
            break
        #else
        else:
            #display enter a valid answer
            print("Please enter valid option")
            continue

#funtion to enter_username()
def enter_username(file):
    #while true
    while True:
        #have user enter a username
        username = input("Enter your username")
        #if username is not saved in json file
        if username not in file:
            #call check
            check_account(file)
        #else
        else:
            #call login
            login()

#function to check_username()
def check_username(file):
    #while true
    while True:
        #ask user (y) to renter username or (n) to create an account
        user = stupid_proofed_inputs("press (y) to renter username or (n) to create an account (r) to restart the login prosses: ", "lower", "y", "n" ,"r")
            #if user entered (y)
        if user == "y":
            #call enter_username funtion
            enter_username()
        #else if user entered n
        elif user == "n":    
            #call create()
            create()
        elif user == "r":
            #call login
            login()
        #else
        else:            
            #display enter a valid option
            print("Enter valid option")
            #continue
            continue
        

#function for creating an account as "create()"
def create(file):
    #while code is not false
    while True:
        #user enter username
        enter_username = stupid_proofed_inputs("Enter your username: ", "none", "_")
        #if username not saved
        if enter_username not in file:
            #save username in json file
            #display username saved
            print(f"{enter_username} saved")
            #user enter password for username
            enter_pass = stupid_proofed_inputs(f"Enter your password for {enter_username}: ", "none", "_")
            user_data = [enter_username, enter_pass]
            #save as ("username": user_username, "password": user_password) in Json file
            user_data_saving(user_data)
        else:
            print(f"Username: {enter_username} already used")


#login function
def login(file):
    #while code not false run till false
    while True:
        #user enter username
        username = input("Enter your username: ")
        #user enter password
        user_pass = stupid_proofed_inputs("Enter your password: ", "none", "_")
        #if user_password does not match username
        if user_pass or username not in file:
            #check_password
            check_username()
    
        #else
        #call the game main file

#function for checking password as "check_passord()"
def check_password():
    #while true
    while True:
        #display enter 1 to re-enter password, 2 to re-enter username, 3 to make an account
        user_clare = input("Enter 1 to re-enter password\n2 to re-enter username\n3 to make an account\n4 to quit")
        #if user entered 1
        if user_clare == "1":
            #call login funtion
            login()
        #else if user entered 2
        elif user_clare == "2":
            #call enter username
            enter_username()
        #else if user entered 3
        elif user_clare == "3":
            #call create
            create()
        elif user_clare == "4":
            #quit message and quit
            print("Good bye")
            break
        #else
        else:
            #display enter a vailid answer
            print("Enter valid answer")
            continue

#funtion for checking account
def check_account(file):
    while True:
        user_check = input("Enter something to search your name (Letter, Number, Word, exedra)")
        #if username is saved
        if user_check in file:
            print("file user_chec")
            check = input("Do you see your username? (Y/N): ").lower
            if check == "y":
                ask = input("Do you want to enter your username? (Y/N): ").lower
                if ask == "y":
                    #call login
                    login()
