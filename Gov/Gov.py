# GNB - 1st - Score format thing so it looks cutie-patootie
import csv
from Parker_stuff import csv_reader

#format = three headers = rank, username, score

#Read CSV from Parker's side about the scores


#Define function read_scores_from_csv(file_path)
def score_order():
    rows = csv_reader()
    ordered_rows = []
    for row in rows:
        ordered_rows.insert(row["rank number"], row)
    return ordered_rows




#Define function (scores_list)
def scores_list():
    ordered_rows = score_order()
    print("===== HIGH SCORES =====")
#    Print "===== HIGH SCORES =====" 

#    Sort scores_list by wins (highest first)
    for ordered_row in ordered_rows:
        print(f"RANK NUMBER {ordered_row["rank number"]} == USERNAME {ordered_row["username"]} == P1 SCORE {ordered_row["player one score"]} == P2 SCORE {ordered_row["player two score"]} == PLAYED AGAINST BOT? {ordered_row["Bot"]}")
    


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
