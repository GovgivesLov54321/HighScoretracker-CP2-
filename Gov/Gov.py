# GNB - 1st - Score format thing so it looks cutie-patootie

from Parker_stuff import csv_reader

#format = three headers = rank, username, score

#Read CSV from Parker's side about the scores

#*USEFUL MENTION* I sorted them so don't worry about it anymore

#Define function (scores_list)
def scores_list(csv_rows):
    print("===== HIGH SCORES =====")
#    Print "===== HIGH SCORES =====" 

#    Sort scores_list by wins (highest first)
    for row in csv_rows:
        print(f"RANK NUMBER {row["rank number"]} == USERNAME {row["username"]} == P1 SCORE {row["player one score"]} == P2 SCORE {row["player two score"]} == PLAYED AGAINST BOT? {row["Bot"]} == RATIO FOR SCORING: {row["ratio"]}")
    
