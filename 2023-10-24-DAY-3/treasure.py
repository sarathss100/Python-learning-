print('''
*******************************************************************************
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
*******************************************************************************
''')

print("Welcome to Treasure island! \n Your mission is to find the treasure")

cross_road = input("You are at a cross road, Please choose left or right \n")

if cross_road == "left":
    lake = input("You are at lake side. to get the other side of the what would you do swim or wait \n")
    if lake == "wait":
        castle = input("You are in front of a castle, and there is three doors. Red, yellow, blue, which one you wish to choose yellow, red or blue?\n")
        if castle == "yellow":
            print("You Win!")
        elif castle == "red":
            print('You are Burned by fire, Game Over!')
        elif castle == "blue":
            print("You are eaten by beasts, Game Over!")
        else:
            print("Game over!")
    else:
        print("You are attacked by trout, Game Over!")
else:
    print("You are fall into a hole Game Over!")