print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
******************************************************************************* ''')
print("Welcome to Treasure Island")
print("Your Mission is to find the Treasure.")
side=input("You're at a crossroad, where do you want to go ? type 'left' or 'right'\n").lower()

if side=="left":

    ch=input('You\'ve come to a lake. there is an island in the middle of the lake.\n type "wait" to wait for a boat. type "swim" to swim across.\n').lower()
    if(ch=="wait"):
        choice=input("you arrive at the island unharmed. There is a house with 3 doors . One red, one yellow, one blue.\n")
        if choice=="red":
            print("It's a room full of fire. Game Over.")
        elif choice=="blue":
            print("you entered a room full of beasts. Game Over.")
        elif choice=="yellow":
            print("You found the treasure! You Win!!")
        else:
            print("You choose a door that doesn't exit. Game Over")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("you fell into a hole. Game Over.")


input("Press Enter to exit: ")