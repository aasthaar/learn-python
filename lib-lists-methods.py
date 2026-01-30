import random

def choices():
    my_choice = input("Enter your choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    comp_choice = random.choice(options)
    choice = {"my_choice": my_choice, "comp_choice": comp_choice}
    return choice

choice = choices()
# print(choice)

# food = ["pizza", "burger", "fries"]
# dinner = random.choice(food)
# print(dinner)

def check_win(player, computer):
    print(f"You chose: {player}, and the computer chose: {computer}")
    if(player == computer):
        return "It's a tie!"
    elif(player == "rock"):
        if(computer == "scissors"):
            return "You win!"
        else:
            return "Computer wins!"
    elif(player == "paper"):
        if(computer == "rock"):
            return "You win!"
        else:
            return "Computer wins!"
    elif(player == "scissors"):
        if(computer == "paper"):
            return "You win!"
        else:
            return "Computer wins!"
        
result = check_win(choice["my_choice"], choice["comp_choice"])
print(result)