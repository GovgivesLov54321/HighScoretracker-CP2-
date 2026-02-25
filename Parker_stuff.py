#PS 1st This is where I code

from Lizards_helper_funcs import *
import hashlib
import csv
#more info: add a rank for each score to the csv so it will be formatted like the following: (rank number),(username),(player one score),(player 2 score), (was player two a bot), (win to lose ratio)

#reader func for csv
def csv_reader():
    #open the file for writing
    with open("Files/score_data.csv", "r") as scores:
        #make each of the lines a list
        rows = scores.readlines()
    #return the list
    return rows


#function for score formating in csv
def score_formats(csv_rows):
    #loop for each item
    for x in csv_rows:
        #calculate the win to lose ratio for each score
        win_lose = x[2]/x[3]
        x.append(win_lose)

    #for each new item
    for x in csv_rows:
        #for each original item
        for y in csv_rows:
            #compare the new item to the original item via the win/lose ratio
            if x[5] == y[5]:
                continue
            #if the new item is higher
            if x[5] > y[5]:
                #make the rank higher than the original item
                x[0]+=1
            #if it is not higher
            if x[5] < y[5]:
                #make the rank lower than the original item
                x[0]-=1
    #write all the data to the csv file
    with open("Files/score_data.csv", "w") as file:
        file.writelines("rank number","username","player one score","player two score","Bot","ratio")
        file.writelines(csv_rows)
    #return the list of properly ranked stuff
    return csv_rows


#user ID finder
    #open the json file to access the last entry
        #find the last user on it and find their user id
    #return the number after it



#JSON file saving func (list of user information)
    #call user ID finder
    #open the JSON with the writing and reading mode and make a dictionary with the current user information
        #create a new user dictionary with all data taken from bg2's user creation screen
        #add that dictionary to the end of the current JSON dictionary
        #upload that new dictionary to the JSON
