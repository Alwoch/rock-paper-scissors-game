import random


#declaring functions and variables
#dictionaries:store data values in key value pairs
#input function allows a user prompt
#outputting strings can be cone either by concatenation or by using fstrings
def get_choices():
  player_choice = input("Enter a choice(rock,paper,scissors)")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices


play = get_choices()
print(play)

def check_win(player,computer):
  print(f"you chose {player} and the computer chose {computer}")
  if player==computer:
    return "its a tie!"
  elif player=="rock":
    if computer=="scissors":
      return "rock smashes scissors, you win!"
    else:
      return "paper covers rock, you lose!"
  elif player=="paper":
    if computer=="rock":
      return "paper covers rock,you win!"
    else:
      return "sccissor cuts paper,you lose!"
  elif player=="scissors":
    if computer=="paper":
      return "scissor cuts paper,you win!"
    else:
      return "rock smashes scissors,you lose!"


