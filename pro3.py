with open("words.txt") as file:
    words = file.read().split()
import random


import tkinter as tk
from tkinter import messagebox
word = random.choice(words)
guessed = []
attempts = 6

# Main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x500")

# Display word
display_word = ["_"] * len(word)

word_label = tk.Label(root, text=" ".join(display_word), font=("Arial", 24))
word_label.pack(pady=20)

attempts_label = tk.Label(root, text=f"Attempts Left: {attempts}", font=("Arial", 14))
attempts_label.pack()

# Function to handle guesses
def guess_letter(letter):
    global attempts

    if letter in guessed:
        return

    guessed.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display_word[i] = letter
        word_label.config(text=" ".join(display_word))
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts Left: {attempts}")

    if "_" not in display_word:
        messagebox.showinfo("Hangman", "🎉 You Won!")
        root.destroy()

    if attempts == 0:
        messagebox.showerror("Hangman", f"💀 You Lost! Word was: {word}")
        root.destroy()

# Buttons A-Z
frame = tk.Frame(root)
frame.pack(pady=20)

for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    btn = tk.Button(frame, text=letter.upper(), width=4,
                    command=lambda l=letter: guess_letter(l))
    btn.grid(row=i // 6, column=i % 6, padx=5, pady=5)

root.mainloop()
