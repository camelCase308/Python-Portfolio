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
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')
print('Welcome to Treasure Island!\nYour mission is to find the treasure!')
direction = input('You are at a crossroad, where do you want to go? Type "Left" or "Right"? ').lower()

if direction == 'left':
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat or "swim" to swim. ').lower()
    if lake == 'wait':
        house = input('You arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow, and one blue.\nWhich color do you choose. ').lower()
        if house == 'red':
            print('It\'s a room full of fire. Game over.')
        elif house == 'yellow':
            print('You found the treasure. You win!')
        elif house == 'blue':
            print('You got eaten by lions. Game over.')
        else:
            print('You lost. Game over.')        
    else:
        print('You\'ve drowned. Game over.')
else:
    print('You fell into a hole. Game over.')
