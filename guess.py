import tkinter as tk
import random

def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        if guess < generated_number - 5 or guess > generated_number + 5:
            result_label.config(text=f"Too far! Try again.\nHints:\n1. The number is between {generated_number - 5} and {generated_number + 5}.\n2. It is {is_prime(generated_number)}.")
        elif guess < generated_number:
            result_label.config(text=f"Too low! Try again.\nHints:\n1. The number is between {generated_number - 5} and {generated_number + 5}.\n2. It is {is_prime(generated_number)}.")
        elif guess > generated_number:
            result_label.config(text=f"Too high! Try again.\nHints:\n1. The number is between {generated_number - 5} and {generated_number + 5}.\n2. It is {is_prime(generated_number)}.")
        else:
            result_label.config(text=f"Congratulations! You guessed the number {generated_number} in {attempts} attempts.\n")
            guess_entry.delete(0, tk.END)
            guess_entry.config(state=tk.DISABLED)
            check_button.config(state=tk.DISABLED)
            play_again_button.config(state=tk.NORMAL)
    except ValueError:
        result_label.config(text="Invalid input! Please enter a number.")

def is_prime(n):
    if n < 2:
        return "not prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "not prime"
    return "prime"

def play_again():
    global generated_number, attempts
    generated_number = random.randint(1, 100)
    attempts = 0
    guess_entry.config(state=tk.NORMAL)
    check_button.config(state=tk.NORMAL)
    result_label.config(text="")
    hint_label.config(text=f"Hints:\n1. The number is between {generated_number - 5} and {generated_number + 5}.\n2. It is {is_prime(generated_number)}.")
    play_again_button.config(state=tk.DISABLED)

generated_number = random.randint(1, 100)
attempts = 0

root = tk.Tk()
root.title("Guessing Game")

guess_label = tk.Label(root, text="Enter your guess:")
guess_label.pack()

guess_entry = tk.Entry(root, width=20)
guess_entry.pack()

hint_label = tk.Label(root, text=f"Hints:\n1. The number is between {generated_number - 5} and {generated_number + 5}.\n2. It is {is_prime(generated_number)}.")
hint_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack()

play_again_button = tk.Button(root, text="Play Again", state=tk.DISABLED, command=play_again)
play_again_button.pack()

root.mainloop()
