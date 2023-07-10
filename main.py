import tkinter
from tkinter import *
from tkinter import messagebox,simpledialog
import csv

root = Tk()
root.title("CRICKET SCORE BOARD")
#Batting
batting_name=Label(root, text="Batsman Name",bg="blue",fg="white")
batting_name.grid(row=1,column=0,padx=5,pady=5)

batting_name_entry=Entry(root,bg="light blue")
batting_name_entry.grid(row=1,column=1,padx=5,pady=5)

batting_runs=Label(root,text="Runs scored",bg="blue",fg="white")
batting_runs.grid(row=2,column=0,padx=5,pady=5)

batting_runs_entry=Entry(root,bg="light blue")
batting_runs_entry.grid(row=2,column=1,padx=5,pady=5)

batting_balls=Label(root,text="Balls faced",bg="blue",fg="white")
batting_balls.grid(row=3,column=0,padx=5,pady=5)

batting_balls_entry=Entry(root,bg="light blue")
batting_balls_entry.grid(row=3,column=1,padx=5,pady=5)

batting_fours=Label(root,text="4s",bg="blue",fg="white")
batting_fours.grid(row=4,column=0,padx=5,pady=5)

batting_fours_entry=Entry(root,bg="light blue")
batting_fours_entry.grid(row=4,column=1,padx=5,pady=5)

batting_sixes=Label(root,text="6s",bg="blue",fg="white")
batting_sixes.grid(row=5,column=0,padx=5,pady=5)

batting_sixes_entry=Entry(root,bg="light blue")
batting_sixes_entry.grid(row=5,column=1,padx=5,pady=5)

batting_dot=Label(root,text="Dot balls",bg="blue",fg="white")
batting_dot.grid(row=6,column=0,padx=5,pady=5)

batting_dot_entry=Entry(root,bg="light blue")
batting_dot_entry.grid(row=6,column=1,padx=5,pady=5)

#Bowling

bowling_name=Label(root,text="Bowler Name",bg="green",fg="white")
bowling_name.grid(row=8,column=0,padx=5,pady=5)

bowling_name_entry=Entry(root,bg="light green")
bowling_name_entry.grid(row=8,column=1,padx=5,pady=5)

bowling_wickets=Label(root,text="Wickets",bg="green",fg="white")
bowling_wickets.grid(row=9,column=0,padx=5,pady=5)

bowling_wickets_entry=Entry(root,bg="light green")
bowling_wickets_entry.grid(row=9,column=1,padx=5,pady=5)

bowling_overs=Label(root,text="Overs",bg="green",fg="white")
bowling_overs.grid(row=10,column=0,padx=5,pady=5)

bowling_overs_entry=Entry(root,bg="light green")
bowling_overs_entry.grid(row=10,column=1,padx=5,pady=5)

bowling_runs=Label(root,text="Runs conceded",bg="green",fg="white")
bowling_runs.grid(row=11,column=0,padx=5,pady=5)

bowling_runs_entry=Entry(root,bg="light green")
bowling_runs_entry.grid(row=11,column=1,padx=5,pady=5)

bowling_dot_balls=Label(root,text="Economy",bg="green",fg="white")
bowling_dot_balls.grid(row=12,column=0,padx=5,pady=5)

bowling_dot_balls_entry=Entry(root,bg="light green")
bowling_dot_balls_entry.grid(row=12,column=1,padx=5,pady=5)

bowling_maiden=Label(root,text="Maiden Overs",bg="green",fg="white")
bowling_maiden.grid(row=13,column=0,padx=5,pady=5)

bowling_maiden_entry=Entry(root,bg="light green")
bowling_maiden_entry.grid(row=13,column=1,padx=5,pady=5)

score_board = Text(root, height=22, width=40,bg="light yellow")
score_board.grid(row=17, column=0, columnspan=8, padx=5, pady=5)

def update_scores():
    #Batting
    bat_name = batting_name_entry.get()
    bat_runs=batting_runs_entry.get()
    bat_balls=batting_balls_entry.get()
    bat_four=batting_fours_entry.get()
    bat_six=batting_sixes_entry.get()
    bat_dot=batting_dot_entry.get()

    #Bowling
    bowl_name=bowling_name_entry.get()
    bowl_wickets=bowling_wickets_entry.get()
    bowl_overs=bowling_overs_entry.get()
    bowl_runs=bowling_runs_entry.get()
    bowl_dot=bowling_dot_balls_entry.get()
    bowl_maiden=bowling_maiden_entry.get()

    score_board.insert(END,f"{bat_name}:{bat_runs}:{bat_balls}:{bat_four}:{bat_six}:{bat_dot}\n")
    score_board.insert(END,f"{bowl_name}:{bowl_wickets}:{bowl_overs}:{bowl_runs}:{bowl_dot}:{bowl_maiden}\n")
    score_board.insert(END, "--------------------------------------------------------------------------------\n")
    #Batting
    batting_name_entry.delete(0,END)
    batting_runs_entry.delete(0,END)
    batting_balls_entry.delete(0,END)
    batting_fours_entry.delete(0,END)
    batting_sixes_entry.delete(0,END)
    batting_dot_entry.delete(0,END)
    #Bowling
    bowling_name_entry.delete(0,END)
    bowling_wickets_entry.delete(0,END)
    bowling_overs_entry.delete(0,END)
    bowling_runs_entry.delete(0,END)
    bowling_dot_balls_entry.delete(0,END)
    bowling_maiden_entry.delete(0,END)

def save_scores():
    
    scores = score_board.get("1.0", END)
    with open("score_sheet.csv", "w") as file:
       file.write(scores)
       messagebox.showinfo("Score Board", "Scores saved to file.")

def delete_scores():
    start_line=simpledialog.askinteger("Delete scores","Enter the line number to delete")
    end_line=simpledialog.askinteger("Delete scores","Enter the ending line number to delete")

    if start_line is not None and end_line is not None:
        score_board.delete(f"{start_line}:{end_line+1}.0")


Batting_text=Label(root,text="BATTING SCORECARD",bg="yellow",fg="black")
Batting_text.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

Bowling_text = Label(root, text="BOWLING SCORECARD",bg="magenta",fg="black") 
Bowling_text.grid(row=7, column=0, columnspan=4, padx=5, pady=10)

update_scores_btn=Button(root,text="Update Scores",command=update_scores,bg="DarkGray",fg="black")
update_scores_btn.grid(row=14,column=0,padx=5,pady=5)

save_scores_btn = Button(root, text="Save Scores", command=save_scores,bg="DarkGray",fg="black")
save_scores_btn.grid(row=14, column=1, padx=5, pady=10)

delete_scores_btn = Button(root, text="Delete Scores", command=delete_scores, bg="DarkGray", fg="black")
delete_scores_btn.grid(row=14, column=2, columnspan=8, padx=5, pady=10)



root.mainloop()


# # batting_frame = LabelFrame(root, text="Batting Stats")
# # batting_frame.pack(padx=10, pady=10)


# # batting_labels = ["Player Name:", "Runs Scored:", "Balls Faced:", "4s","6s","Dot balls:"]
# # batting_entries = []

# for i, label_text in enumerate(batting_labels):
#     label = Label(batting_frame, text=label_text)
#     label.grid(row=i, column=0, sticky=W, padx=5, pady=5)

#     entry = Entry(batting_frame)
#     entry.grid(row=i, column=1, padx=5, pady=5)
#     batting_entries.append(entry)



# bowling_frame = LabelFrame(root, text="Bowling Stats")
# bowling_frame.pack(padx=10, pady=10)

# bowling_labels = ["Player Name:", "Overs Bowled:", "Runs Conceded:", "Wickets Taken:","Dot Balls","Maiden Overs"]
# bowling_entries = []

# for i, label_text in enumerate(bowling_labels):
#     label = Label(bowling_frame, text=label_text)
#     label.grid(row=i, column=0, sticky=W, padx=5, pady=5)

#     entry = Entry(bowling_frame)
#     entry.grid(row=i, column=1, padx=5, pady=5)
#     bowling_entries.append(entry)

# entry = Text(root, height=10, width=40)

# def display_stats():
    
#     batting_player_name = batting_entries[0].get()
#     batting_runs_scored = batting_entries[1].get()
#     batting_balls_faced = batting_entries[2].get()
#     batting_4s=batting_entries[3].get()
#     batting_6s=batting_entries[4].get()
#     batting_dot_balls = batting_entries[5].get()


#     bowling_player_name = bowling_entries[0].get()
#     bowling_overs_bowled = bowling_entries[1].get()
#     bowling_runs_conceded = bowling_entries[2].get()
#     bowling_wickets_taken = bowling_entries[3].get()
#     bowling_maiden_overs=bowling_entries[4].get()
#     bowling_dot_balls=bowling_entries[5].get()

#     entry.insert(END,f"{batting_player_name}:{batting_runs_scored}:{batting_balls_faced}:{batting_4s}:{batting_6s}:{batting_dot_balls}")
#     entry.insert(END,f"{bowling_player_name}:{bowling_overs_bowled}:{bowling_runs_conceded}:{bowling_wickets_taken}:{bowling_maiden_overs}:{bowling_dot_balls}")

   
#     entry.delete(0,END)
#     # batting_player_name.delete(0,END)
#     # batting_runs_scored.delete(0,END)
#     # batting_balls_faced.delete(0,END)
#     # batting_4s.delete(0,END)
#     # batting_6s.delete(0,END)
#     # batting_dot_balls.delete(0,END)

#     # bowling_player_name.delete(0,END)
#     # bowling_overs_bowled.delete(0,END)
#     # bowling_runs_conceded.delete(0,END)
#     # bowling_wickets_taken.delete(0,END)
#     # bowling_maiden_overs.delete(0,END)
#     # bowling_dot_balls.delete(0,END)


#     stats_message = f"Batting Stats:\nPlayer Name: {batting_player_name}\nRuns Scored: {batting_runs_scored}\nBalls Faced: {batting_balls_faced}\n4s: {batting_4s}\n6s: {batting_6s}\nDot Balls:{batting_dot_balls}\n\nBowling Stats:\nPlayer Name: {bowling_player_name}\nOvers Bowled: {bowling_overs_bowled}\nRuns Conceded: {bowling_runs_conceded}\nWickets Taken: {bowling_wickets_taken}\nMaiden Overs:{bowling_maiden_overs}\nDot Balls:{bowling_dot_balls}"
#     messagebox.showinfo("Cricket Stats", stats_message)

# def save_scores():
#      scores = entry.get("1.0", END)
#      with open("scores1.txt", "w") as file:
#          file.write(scores)
#      messagebox.showinfo("Score Board", "Scores saved to file.")

# def delete_scores():
#     start_line = simpledialog.askinteger("Delete Scores", "Enter the starting line number to delete:")
#     end_line = simpledialog.askinteger("Delete Scores", "Enter the ending line number to delete:")
#     if start_line is not None and end_line is not None:
#         entry.delete(f"{start_line}.0", f"{end_line + 1}.0")




# display_button = Button(root, text="Display Stats", command=display_stats)
# display_button.pack(pady=10)

# save_scores_btn = Button(root, text="Save Scores", command=save_scores)
# save_scores_btn.pack(pady=10)

# delete_scores_btn = Button(root, text="Delete Scores", command=delete_scores, bg="red", fg="white")
# delete_scores_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)








# root.mainloop()





# from tkinter import *
# from tkinter import messagebox

# root = Tk()
# root.title("Cricket Score Board")

# team1_label = Label(root, text="Team 1:")
# team1_label.grid(row=0, column=0, padx=5, pady=5)

# team1_entry = Entry(root)
# team1_entry.grid(row=0, column=1, padx=5, pady=5)

# team2_label = Label(root, text="Team 2:")
# team2_label.grid(row=1, column=0, padx=5, pady=5)

# team2_entry = Entry(root)
# team2_entry.grid(row=1, column=1, padx=5, pady=5)

# team1_score_label = Label(root, text="Score:")
# team1_score_label.grid(row=0, column=2, padx=5, pady=5)

# team1_score_entry = Entry(root)
# team1_score_entry.grid(row=0, column=3, padx=5, pady=5)

# team2_score_label = Label(root, text="Score:")
# team2_score_label.grid(row=1, column=2, padx=5, pady=5)

# team2_score_entry = Entry(root)
# team2_score_entry.grid(row=1, column=3, padx=5, pady=5)

# score_board = Text(root, height=10, width=40)
# score_board.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# def update_scores():
#     team1 = team1_entry.get()
#     team2 = team2_entry.get()
#     score1 = team1_score_entry.get()
#     score2 = team2_score_entry.get()

#     score_board.insert(END, f"{team1}: {score1}\n")
#     score_board.insert(END, f"{team2}: {score2}\n")
#     score_board.insert(END, "----------------------\n")

# team1_entry.delete(0, END)
# team2_entry.delete(0, END)
# team1_score_entry.delete(0, END)
# team2_score_entry.delete(0, END)

#  def save_scores():
#      scores = score_board.get("1.0", END)
#      with open("score_sheet.csv", "w") as file:
#          file.write(scores)
#      messagebox.showinfo("Score Board", "Scores saved to file.")

# update_scores_btn = Button(root, text="Update Scores", command=update_scores)
# update_scores_btn.grid(row=2, column=0, columnspan=4, padx=5, pady=10)

# save_scores_btn = Button(root, text="Save Scores", command=save_scores)
# save_scores_btn.grid(row=4, column=0, columnspan=4, padx=5, pady=10)

# root.mainloop()
