#BG 1st code for high score tracker
from Parker_stuff import *
from Lizards_helper_funcs import *
import hashlib
from Gov.tic_tac_toe_remix import *
from Gov.Gov import *

def what():
    with open("HighScoretracker-CP2-\\hi_file.csv", newline='\n') as file:
        fieldnames = ["username", "password"]
        reader = json.reader(file)
#funtion to welcome user as "welcome"
def welcome():
    while True:
        file = JSON_reader()
        #display welcome to the highscore tracker
        print("Welcome to the highscore tracker: ")
        #enter a number 1 to check if you have an account 2 to login 3 to create an account 4 to exit program
        print("1 to check if you have an account\n2 to login\n3 to create an account\n4 to look at the leaderboard\n5 to exit program: ")
        user_in = stupid_proofed_inputs("What do you want to do: ", "number", "1", "2", "3", "4","5")
        #if user entered 1
        if user_in == "1":
            #call enter()
            check_account(file)
        elif user_in == "2":
            login(file)
        #if user entered 3
        elif user_in == "3":
            #call create funtion
            create(file)
        #if user entered 4
        elif user_in == "4":
            #show scores
            scores_list(csv_reader())
        elif user_in == "5":
            #break/leave program
            break
        #else
        else:
            #display enter a valid answer
            print("Please enter valid option: ")
            continue

#funtion to enter_username()
def enter_username(file):
    #while true
    while True:
        #have user enter a username
        username = input("Enter your username: ")
        #if username is not saved in json file
        if username not in file:
            #call check
            check_account(file)
        #else
        else:
            #call login
            login(file)

#function to check_username()
def check_username(file):
    #while true
    while True:
        #ask user (y) to renter username or (n) to create an account
        user = stupid_proofed_inputs("press (y) to renter username or (n) to create an account (r) to restart the login prosses (l) to leave: ", "lower", "y", "n" ,"r", "l")
            #if user entered (y)
        if user == "y":
            #call enter_username funtion
            enter_username(file)
        #else if user entered n
        elif user == "n":    
            #call create()
            #call login
            login(file)
        elif user == "l":
            return
        #else
        else:            
            #display enter a valid option
            print("Enter valid option: ")
            #continue
            continue
        

#function for creating an account as "create()"
def create(file):
    #while code is not false
    while True:
        #user enter username
        username = stupid_proofed_inputs("Enter a username for your account: ", "none", "_")
        if username not in file:
            #save username in json file
            #display use password for username
            enter_pass = stupid_proofed_inputs(f"Enter your password for {username}: ", "none", "_")
            user_data = [username, enter_pass]
            #save as ("username": user_username, "password": user_password) in Json file
            user_data_saving(user_data)
            break
        else:
            print(f"Username: {username} already used: ")


#login function
def login(file):
    #while code not false run till false
    while True:
        #user enter username
        username = stupid_proofed_inputs("Enter your username: ", "none", "_")
        #user enter password
        user_pass = stupid_proofed_inputs("Enter your password: ", "none", "_")
        #if user_password does not match username
        if username in file.keys():
            if hashlib.blake2b(user_pass.encode("utf-8")).hexdigest() == file[username]["password"]:
                #call the game file
                game_stats = play_game()
                game_stats.insert(0,username)
                score_formats(csv_reader(),game_stats)
                break
            else:
                print("Password wrong")
        else:
            print("Username not found")
            break
        



#funtion for checking account
def check_account(file):
    for i in file.keys():
        print(f"usernames: {i}")