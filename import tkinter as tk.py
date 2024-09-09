import tkinter as tk
from random import choice

class HangmanGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman Game")
        self.word_list = ["apple", "banana", "cherry", "date", "elderberry"]
        self.word = choice(self.word_list)
        self.guessed_letters = []
        self.guessed_word = ["_"] * len(self.word)
        self.tries = 6

        self.word_label = tk.Label(self.root, text=" ".join(self.guessed_word), font=("Arial", 24))
        self.word_label.pack()

        self.guess_label = tk.Label(self.root, text="Guess a letter:", font=("Arial", 18))
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.root, font=("Arial", 18))
        self.guess_entry.pack()

        self.result_label = tk.Label(self.root, text="", font=("Arial", 18))
        self.result_label.pack()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.guess_letter)
        self.guess_button.pack()

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack()

    def guess_letter(self):
        letter = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)

        if len(letter) != 1:
            self.result_label.config(text="Please enter a single letter.")
            return

        if letter in self.guessed_letters:
            self.result_label.config(text="You already guessed this letter.")
            return

        self.guessed_letters.append(letter)

        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guessed_word[i] = letter
            self.word_label.config(text=" ".join(self.guessed_word))
            if "_" not in self.guessed_word:
                self.result_label.config(text="Congratulations, you won!")
                self.guess_button.config(state="disabled")
        else:
            self.tries -= 1
            self.result_label.config(text=f"Incorrect! You have {self.tries} tries left.")
            if self.tries == 0:
                self.result_label.config(text=f"Game over! The word was {self.word}.")
                self.guess_button.config(state="disabled")

    def reset_game(self):
        self.word = choice(self.word_list)
        self.guessed_letters = []
        self.guessed_word = ["_"] * len(self.word)
        self.tries = 6
        self.word_label.config(text=" ".join(self.guessed_word))
        self.result_label.config(text="")
        self.guess_button.config(state="normal")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = HangmanGame()
    game.run()