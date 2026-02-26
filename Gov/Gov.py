# GNB - 1st - Score format thing so it looks cutie-patootie
import csv

#format = three headers = rank, username, score

#Read CSV from Parker's side about the scores


#Define function read_scores_from_csv(file_path)
def read_scores_from_csv(file_path):
    with open("path or wtv.csv", "r") as csv_file:
#    TRY to open CSV file
        content = csv.reader(csv_file)
        rows = []

#        READ each row
#        STORE each row as dictionary:
#            name
#            wins
#            losses
#            ties
#        ADD dictionary to scores list
#    IF file does not exist
#        CREATE empty file with header:
#            name,wins,losses,ties
#        RETURN empty list
#    RETURN scores list


#Define function (scores_list)
#    Print "===== HIGH SCORES ====="

#    Sort scores_list by wins (highest first)

#   For each player in scores_list
#        Print formatted line:
#            Name | Wins | Losses | Ties
#        Example:
#            Alex   | 5 Wins | 2 Losses | 1 Tie

#    Print dividing line


#Define function (scores_list, player_name, result)
#    Search scores_list for player_name

#    if player exists
#        if result == win
#            increase wins by 1
#        elif result == loss
#            increase losses by 1
#        elif result == tie
#            increase ties by 1
#    else
#        Create new player dictionary
#            set wins/losses/ties based on result
#        Add to scores_list


#Define function (file_path, scores_list)
#    Open file in write mode
#    Write header row
#    For each player in scores_list
#        Write player data as CSV row


#Main thing

#set file_path to wherever it leads to "scores.csv" or something like that

#Call read_scores_from_csv(file_path)
#Store returned list as scores

#While True
#    Print menu:
#        1. View High Scores
#        2. Add Game Result
#        3. Save Scores
#        4. Exit

#    Get user choice

#    if choice == 1
#        CALL format_scores(scores)

#    If choice == 2
#        ASK for player name
#        ASK for result (win/loss/tie)
#        CALL update_score(scores, name, result)

#    if choice == 3
#        CALL save_scores_to_csv(file_path, scores)

#    If choice == 4
#        ASK if user wants to save before exiting
#        IF yes
#            CALL save_scores_to_csv
#        BREAK loop



#End program
