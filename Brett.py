#Gov Brett Parker

#hi

#funtion to welcome user as "welcome"
    #display welcome to the highscore tracker
    #enter a number 1 to check if you have an account 2 to login 3 to create an account 4 to exit program
    #if user entered 1
        #call enter()
    #if user entered 2
        #call login function
    #if user entered 3
        #call create funtion
    #if user entered 4
        #exit/break program
    #else
        #display enter a valid answer

#funtion to enter_username()
    #while true
        #have user enter a username
        #if username is not saved in json file
            #call check

#function to check_username()
    #while true
        #ask user (y) to renter username or (n) to create an account
            #if user entered (y)
                #call enter
            #else if user entered n
                #call create()
            #else
                #display enter a valid option
                #continue
        #else if username is saved
            #return username
            #call login()

#function for creating an account as "create()"
    #while code is not false
        #user enter username
        #save username in json file
        #display username saved
        #user enter password for username
        #save as ("username": user_username, "password": user_password) in Json file
        #return 

#login function
    #while code not false run till false
        #with username from the enter funtion
            #user enter password
            #if user_password does not match username
                #check_password
            #else
                #call the game file

#function for checking password as "check_passord()"
    #while true
        #display enter 1 to re-enter password, 2 to re-enter username, 3 to make an account
        #if user entered 1
            #call login funtion
        #else if user entered 2
            #call enter
        #else if user entered 3
            #call create
        #else
            #display enter a vailid answer
