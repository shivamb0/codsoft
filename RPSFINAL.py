import tkinter as tk
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_list = [rock, paper, scissors]


def play_round(player_choice):
    cpu_choice = random.randint(0, 2)

    # player choice
    player_choice_text.set(f"Your Choice:\n{choices_list[player_choice]}")

    # comp choice
    cpu_choice_text.set(f"Computer's Choice:\n{choices_list[cpu_choice]}")

    # result
    if (player_choice == 0 and cpu_choice == 2) or \
            (player_choice == 1 and cpu_choice == 0) or \
            (player_choice == 2 and cpu_choice == 1):
        result_text.set("Result: You win!")
    elif player_choice == cpu_choice:
        result_text.set("Result: It's a tie!")
    else:
        result_text.set("Result: You lose!")

    play_again_button.pack(pady=10)


# reset
def reset_game():
    player_choice_text.set("Your Choice:")
    cpu_choice_text.set("Computer's Choice:")
    result_text.set("Result:")
    play_again_button.pack_forget()


# restart
def play_again():
    reset_game()

root = tk.Tk()
root.title("Rock Paper Scissors")

player_choice_text = tk.StringVar(value="Your Choice:")
cpu_choice_text = tk.StringVar(value="Computer's Choice:")
result_text = tk.StringVar(value="Result:")

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), fg="green").pack(pady=10)

# rules
tk.Label(
    root,
    text="Instructions: Choose Rock, Paper, or Scissors. The computer will randomly select a choice. "
         "The winner is decided based on the rules of the game.\nPress 'Play Again' to restart the game.",
    font=("Arial", 10),
    justify="center",
    wraplength=400
).pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

# Rock Button
tk.Button(frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play_round(0)).grid(row=0, column=0,
                                                                                                padx=10)

# Paper Button
tk.Button(frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play_round(1)).grid(row=0, column=1,
                                                                                                 padx=10)

# Scissors Button
tk.Button(frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play_round(2)).grid(row=0, column=2,
                                                                                                    padx=10)

tk.Label(root, textvariable=player_choice_text, font=("Courier", 10), justify="left").pack(pady=5)
tk.Label(root, textvariable=cpu_choice_text, font=("Courier", 10), justify="left").pack(pady=5)
tk.Label(root, textvariable=result_text, font=("Arial", 14, "bold"), fg="blue").pack(pady=10)

# play again Button
play_again_button = tk.Button(root, text="Play Again", font=("Arial", 12), bg="green", fg="white", command=play_again)

root.mainloop()
