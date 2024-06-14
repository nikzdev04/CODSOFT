import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.window.geometry("300x200")
        self.user_score = 0
        self.computer_score = 0
        self.result_label = tk.Label(self.window, text="", font=("Helvetica", 12))
        self.result_label.pack()
        self.score_label = tk.Label(self.window, text="Score - You: 0, Computer: 0", font=("Helvetica", 12))
        self.score_label.pack()
        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT)
        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT)
        self.scissors_button = tk.Button(self.window, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = choice(choices)
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        self.result_label.config(text=f"Computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()