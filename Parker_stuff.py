#PS 1st This is where I code


#more info: add a rank for each score to the csv so it will be formatted like the following: (rank number),(username),(player one score),(player 2 score), (was player two a bot), (win to lose ratio)

#writer func for csv
    #open the file for writing
        #make each of the lines a list
    #return the list


#function for score formating in csv
    #loop for each item
        #calculate the win to lose ratio for each score
    #create a list with all the scores in it
    #for each new item
        #for each original item
            #compare the new item to the original item via the win/lose ratio
            #if the new item is higher
                #make the rank higher than the original item
            #if it is not higher
                #make the rank lower than the original item
    #write all the data to the csv file
    #return the list of properly ranked stuff


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
