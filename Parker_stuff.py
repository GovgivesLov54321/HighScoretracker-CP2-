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
            rows.append({headers[0]:x[0],headers[1]:x[1],headers[2]:x[2],headers[3]:x[3],headers[4]:x[4]})
        #return the list
        return rows

#incoming data (rank number (blank):thing, username:thing,p1 score:thing,p2 score:thing,bot y/n:bool,ratio )
def new_row_format(data):
    ratio = f"{data[1]}:{data[2]}"
    proper_row = {
        "rank number":None,
        "username":data[0],
        "player one score":data[1],
        "player two score":data[2],
        "Bot":data[3],
        "ratio":ratio
    }
    return proper_row



#function for rank finding
def score_formats(csv_rows,new_row):
    rank = 1
    #use the incoming new row which has (blank,username,p1 score, p2 score, p2 bot, win/lose ratio)
    #compare it to all of the other scores currently in the file
    new_row = new_row_format(new_row)
    for x in csv_rows: 
        try:
            if new_row["ratio"] > x["ratio"]:
                rank-=1
            elif new_row["ratio"] < x["ratio"]:
                rank+=1
        except:
            if new_row["ratio"] > csv_rows[4]:
                rank-=1
            elif new_row["ratio"] < csv_rows[4]:
                rank+=1
    csv_rows.append(new_row)
    #write all the data to the csv file
    with open("Files/score_data.csv", "w") as file:
        fieldnames = ["rank number","username","player one score","player two score","Bot","ratio"]
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        for x in csv_rows:
            writer.writerow({"rank number":x["rank number"],"username":x["username"],"player one score":x["player one score"],"player two score":x["player two score"],"Bot":x["Bot"],"ratio":x["ratio"]})
    #return the list of properly ranked stuff
    return csv_rows


#user ID finder
def ID_find():
    #open the json file to access the last entry
    with open("Files/user_data.json", "r") as user_data:
        data = json.load(user_data)
        #find the last user on it and find their user id
        key_list = list(data.keys())
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
    with open("Files/user_data.json", "r+") as user_data:
        #create a new user dictionary with all data taken from bg2's user creation screen
        user_info[1] = user_info[1].encode("utf-8")
        user = {
            "username":user_info[0],
            "password":hashlib.blake2b(user_info[1]).hexdigest(),
            "user id":id
        }
        data = json.load(user_data)
        data[user_info[0]] = user
        user_data.truncate(0)
        user_data.seek(0)
        #upload that new dictionary to the JSON
        json.dump(data,user_data,indent=4)


#JSON reader
def JSON_reader():
    with open("Files/user_data.json","r") as user_info:
        data = json.load(user_info)
        return data