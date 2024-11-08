print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are in front of a path full of roses with big thorns that's splits in two")
first_choice = input("Which path you want to go: Type left or right ")
if first_choice == "left":
    print("You are now in a lake. There is an island in the middle of the lake.")
    second_choice = input("Type 'wait' to wait for a boat. Type 'swim' to swim across:  ")
    if second_choice == 'wait':
        print("You are now at the island and there are 3 different colored doors: red, yellow, blue.")
        third_choice = input("Which door would you like to open: Type red, yellow or blue:  ")
        if third_choice == 'yellow':
            print("You have found the treasure..!! You Win..!!")
        elif third_choice == 'red':
            print("You have opened the wrong door. A Dragon just ate you..!!. You Lose..!!")
        elif third_choice == 'blue':
            print("You have opened the wrong door. A room full snakes just kill you..!!. You Lose..!!")
        else:
            print("You have typed an incorrect choice")

    elif second_choice == 'swim':
        print("You have been attacked by a big Shark. You Lose..!!")
    else:
        print("You have typed an incorrect choice")
elif first_choice == 'right':
    print("You have fallen in front of a big angry and hungry bear and died.  You Lose..!!")
else:
    print("You have typed an incorrect choice")
