import time
import random

enemies = ["Dragon", "Goblin", "Troll", "Giant Spider", "Demon"]
enemy = random.choice(enemies)

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt)
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Please choose a valid response (Enter 1 or 2.)")
    return response

def play_again(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        if option2 in response:
            break
        else:
            print_pause("Please choose a valid response (Enter y or n.)")
    return response


def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To the right is a dark musky cave.")
    print_pause("In your hand you hold your dagger.")
    print_pause("What should you do next?")


def house(items):
    if "Mysterious Sword" in items:
        print_pause("You feel more confidhowent then usual and you proceed to break through the door of the house.")
        print_pause(f"After breaking through the door of the house the {enemy} stands in front of you trembling.")
        print_pause("The power of the Mysterious Sword courses through your veins. You feel stronger then ever.")
        choice = valid_input("Would you like to (1) fight or (2) run away?\n", '1', '2')
        if choice == '1':
            fight(items)
        elif choice == '2':
            print_pause("You attempt to run away.")
            print_pause("The attempt was successful!")
            print_pause("You are back in the field.")
            make_choice(items)
    else:
        print_pause("You approach the door of the house.")
        print_pause(f"You are about to knock when the door opens and out steps the {enemy}.")
        print_pause(f"Eep! This is the {enemy}'s house!")
        print_pause(f"The {enemy} gets ready to attack.")
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
        choice = valid_input("Would you like to (1) fight or (2) run away?\n", '1', '2')
        if choice == '1':
            fight(items)
        elif choice == '2':
            print_pause("You attempt to run away.")
            print_pause("The attempt was successful!")
            print_pause("You are back in the field.")
            make_choice(items)

def cave(items):
    if "Mysterious Sword" in items:
        print_pause("You have been here before. There is nothing else here.")
        print_pause("You walk back out to the field.")
        make_choice(items)

    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a small cave.")
        print_pause("Your eye catches a glimpse of metal behind a rock.")
        print_pause("You have found a Mysterious Sword!")
        print_pause("You pick up the Sword and discard your dagger.")
        items.append("Mysterious Sword")
        print_pause("You walk back out to the field.")
        make_choice(items)



def fight(items):
    print_pause(f"You prepare to fight the ghastly {enemy}.")
    if "Mysterious Sword" in items:
        print_pause("The power of the sword engulfs you in flames!")
        print_pause("However you feel nothing but confidence.")
        print_pause("You raise the sword up to swing.")
        print_pause(f"A giant fire blast comes out of the sword and disingrates the {enemy}!")
        print_pause(f"Congratulations! You have slain the {enemy}.")
        print_pause("You go to the village to celebrate.")
        print_pause("The End.")
        choice = play_again("Would you like to play again? (y/n)", 'y', 'n')
        if "y" in choice:
            play_game()
        if "n" in choice:
            print_pause("Have a good day! Thanks for playing!")
    else:
        print_pause(f"You take a swing at the {enemy} with your dagger.")
        print_pause(f"The dagger broke in half after making contact, doing nothing to the {enemy}.")
        print_pause(f"The {enemy} laughs loudly, and kills you.")
        print_pause("Game over.")
        choice = play_again("Would you like to play again? (y/n)", 'y', 'n')
        if "y" in choice:
            play_game()
        if "n" in choice:
            print_pause("Have a good day! Thanks for playing!")


def make_choice(items):
    print_pause("Enter 1 to knock on door of the house.\n"
    "Enter 2 to peer into cave.")
    choice = valid_input("(Please enter 1 or 2.) ", '1', '2')
    if choice == '1':
        house(items)
    elif choice =='2':
        cave(items)


def play_game():
    items = []
    intro()
    make_choice(items)

play_game()
