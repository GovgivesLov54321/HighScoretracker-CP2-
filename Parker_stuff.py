#PS 1st This is where I code

from Lizards_helper_funcs import *
import hashlib
import csv
import json
#more info: add a rank for each score to the csv so it will be formatted like the following: (rank number),(username),(player one score),(player 2 score), (was player two a bot), (win to lose ratio)

#reader func for csv
def csv_reader():
    #open the file for reading
    with open("Files/score_data.csv", mode="r") as scores:
        content = csv.reader(scores)
        headers = next(content)
        rows = []

        #make each of the lines a list of dictionaries
        for x in content:
            rows.append({headers[0]:x[0],headers[1]:x[1],headers[2]:x[2],headers[3]:x[3],headers[4]:x[4],headers[5]:x[5]})
        #return the list
        return rows

#incoming data (rank number (blank):thing, username:thing,p1 score:thing,p2 score:thing,bot y/n:bool,ratio )
def new_row_format(data):
    proper_row = {
        "rank number":None,
        "username":data[0],
        "player one score":data[1],
        "player two score":data[2],
        "Bot":data[3],
        "ratio":data[1]/data[2]
    }
    return proper_row



#function for rank finding
def score_formats(csv_rows,new_row):
    rank = 1
    #use the incoming new row which has (blank,username,p1 score, p2 score, p2 bot, win/lose ratio)
    #compare it to all of the other scores currently in the file
    for x in csv_rows: 
        if new_row["ratio"] > x["ratio"]:
            print("REPLACE THIS WITH CODE: put score above this")
        elif new_row["ratio"] < x["ratio"]:
            print("REPLACE THIS WITH CODE: put score below this")
        else:
            print("keep the rank the same")
    #write all the data to the csv file
    with open("Files/score_data.csv", "w") as file:
        file.writelines("rank number","username","player one score","player two score","Bot","ratio")
        file.writelines(csv_rows)
    #return the list of properly ranked stuff
    return csv_rows


#user ID finder
def ID_find():
    #open the json file to access the last entry
    with open("Files/user_data.json", "r") as user_data:
        data = json.load(user_data)
        #find the last user on it and find their user id
        key_list = data.keys()
        final_index = len(key_list)-1
        final_key = key_list[final_index]
        user_id = data[final_key]["user id"]+1
    #return the number after it
        return user_id



#JSON file saving func (list of user information)
def user_data_saving(user_info):
    #call user ID finder
    id = ID_find()
    #open the JSON with the writing and reading mode and make a dictionary with the current user information
    with open("Files/user_data.json", "a") as user_data:
        #create a new user dictionary with all data taken from bg2's user creation screen
        user = {
            "username":user_info[0],
            "password":hashlib.blake2b(user_info[1]),
            "user id":id
        }
        #add that dictionary to the end of the current JSON dictionary
        data = json.load(user_data)
        data.append(user)
        #upload that new dictionary to the JSON
        json.dump(data,user_data,indent=4)
