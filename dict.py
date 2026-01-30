def choices():
    # choice = {"my_choice": "rock", "comp_choice": "paper"}
    my_choice = input("Enter your choice (rock, paper, scissors): ")
    comp_choice = "paper"
    choice = {"my_choice": my_choice, "comp_choice": comp_choice}
    return choice

choice = choices()
print(choice["my_choice"])
print(choice["comp_choice"])