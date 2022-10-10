import random


#declaring functions and variables
def get_choices():
  player_choice = input("Enter a choice(rock,paper,scissors)")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices


play = get_choices()
print(play)
#dictionaries:store data values in key value pairs
#input function allows a user prompt
#outputting strings can be cone either by concatenation or by using fstrings eg

age = 20
print(f"Jim is {age} years old")
