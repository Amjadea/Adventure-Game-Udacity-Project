import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, option):
    print_pause("You awaken on what seems like a deserted island.")
    print_pause("The boat you were on has crashed, "
                "but thankfully you washed up on the shore.")
    print_pause("As you venture into the isalnd exploring, "
                "you notice a brightly lit mansion from afar.")
    print_pause("For all you know a " + option + " could live there, "
                "but you just have to find a shelter, "
                "some food and materials to build a raft.")
    print_pause("The mansion is right in front of you.")
    print_pause("On your left is a small shed probably used for storage.")
    print_pause("You have on you a pocket knife that you take "
                "with you everywhere for protection.\n")


def shed(item, option):
    if "gun" in item:
        print_pause("\nYou go in to check out the shed one last time")
        print_pause("You browse the rest of the weapons, "
                    "but decide to stick with the gun you have for now.")
        print_pause("You walk back out.\n")
    else:
        print_pause("\nYou decide you should checkout the shed first.")
        print_pause("It turns out it's an arsenal!")
        print_pause("You are terrified to go in armed "
                    "with only a pocket knife.")
        print_pause("You don't know how to use guns, "
                    "but you pick out the one that seems easiest to handle, ")
        print_pause("and discard your pocket knife "
                    "to make room for an extra clip.")
        print_pause("You walk back out.\n")
        item.append("gun")
    out(item, option)


def mansion(item, option):
    print_pause("\nYou approach the gate of the mansion.")
    print_pause("You are about to ring the bell when the gate "
                "opens and out steps a " + option + ".")
    print_pause("Who dares trespass on the " + option + "'s property!\n")
    if "gun" not in item:
        print_pause("You fear your pocket knife isn't enough "
                    "to take care of this situation.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "escape?\n")
        if choice2 == "1":
            if "gun" in item:
                print_pause("\nAs the " + option + " moves to attack, "
                            "you begin to raise your new weapon.")
                print_pause("Your hands shake as you remember "
                            "you've never fired a gun before.")
                print_pause("But you stand your ground and aim.")
                print_pause("Terrified, the " + option + " runs away"
                            "begging you not to shoot.")
                print_pause("The mansion is all yours now."
                            "Hopefully you can find all materials "
                            "necessary to get you home.\n")
            else:
                print_pause("\nYou give it your best try with the knife.")
                print_pause("But it's too weak to harm the " + option + ".")
                print_pause("\nYou lost the fight!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back towards the shore.")
            print_pause("You will have to find another way "
                        "to get the food and materials you need, "
                        "but at least you are alive.\n")
            out(item, option)
            break


def out(item, option):
    print_pause("Enter 1 to ring the mansion's bell.")
    print_pause("Enter 2 to check out the shed.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            mansion(item, option)
            break
        elif choice1 == "2":
            shed(item, option)
            break


def play_game():
    item = []
    option = random.choice(["giant", "zombie", "vampire", "witch",
                            "dragon"])
    intro(item, option)
    out(item, option)


def play_again():
    again = input("Wanna play again? (y/n)\n").lower()
    if again == "y":
        print_pause("\n\n\nFantastic! Stand by while the game restarts\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThank you for playing!\n\n\n")
    else:
        play_again()


play_game()
