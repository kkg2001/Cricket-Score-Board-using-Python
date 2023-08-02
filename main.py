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

    score_board.insert(END,f"{bat_name},{bat_runs},{bat_balls},{bat_four},{bat_six},{bat_dot}\n")
    score_board.insert(END,f"{bowl_name},{bowl_wickets},{bowl_overs},{bowl_runs},{bowl_dot},{bowl_maiden}\n")
    score_board.insert(END, "--------------------------------------------------------------------------------\n")

def save_scores():
    
    scores = score_board.get("1.0", END)
    with open("score_sheet.csv", "w") as file:
       file.write(scores)
       messagebox.showinfo("Score Board", "Scores saved to file.")

def delete_scores():
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


