import tkinter as tk
from tkinter import messagebox
import random

def computer_selection ():
    choix = ["Rock", "Paper", "Scissors"]
    return random.choice(choix)

def find_winner(userChoice, computer_choice):
    if userChoice == computer_choice:
        return "Tie"
    elif (userChoice == "Rock" and computer_choice == "Scissors") or (userChoice == "Scissors" and computer_choice == "Paper") or (userChoice == "Paper" and computer_choice == "Rock"):
        return "Win"
    else:
        return "Lose"
def play(userChoice):
    computer_choice = computer_selection()
    result = find_winner(userChoice, computer_choice)
    user_label.config(text=f"You choose : {userChoice}")
    computer_label.config(text=f"The computer choose : {computer_choice}")
    result_label.config(text=result)

    if result == "Win":
        scores["User"] += 1
    elif result == "Lose":
        scores["Computer"] += 1

    label_scores.config(text=f"Scores:  User {scores['User']} - Computer {scores['Computer']}")

def reset_game():
    scores["User"] = 0
    scores["Computer"] = 0
    user_label.config(text="")
    computer_label.config(text="")
    result_label.config(text="")
    label_scores.config(text=f"Scores: User {scores["User"]} - Computer {scores["Computer"]}")


root = tk.Tk() 
root.title("ROCK, PAPER, SCISSORS GAME")

scores = {"User" : 0, "Computer" :0}
user_label = tk.Label(root, text="", font=("Helvetica", 14))
user_label.pack()

computer_label = tk.Label(root, text="", font=("Helvetica", 14))
computer_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack()

label_scores = tk.Label(root, text=f"Scores: User {scores['User']} - Computer {scores['Computer']}", font=("Helvetica", 14))
label_scores.pack()

btn_rock = tk.Button(root, text="Rock", command=lambda: play("Rock"), font=("Helvetica", 14))
btn_rock.pack(side=tk.LEFT, padx=20)
btn_paper = tk.Button(root, text="Paper", command=lambda: play("Paper"), font=("Helvetica", 14))
btn_paper.pack(side=tk.LEFT, padx=20)
btn_scissors = tk.Button(root, text="Scissors", command=lambda: play("Scissors"), font=("Helvetica", 14))
btn_scissors.pack(side=tk.LEFT, padx=20)

btn_reset = tk.Button(root, text="Reset", command=reset_game, font=("Helvetica", 14))
btn_reset.pack(side=tk.BOTTOM, pady=20)

root.mainloop()