import os

"Story"


print("Hello User")
yourName = input("What is your name? ==> ")
os.system("clear")
print("Hello " + yourName + ", Welcome to your 1,262th day at WAL-MART!")
input("-- Press enter to continue --")
os.system("clear")
print(yourName + " has walked up to the cash register and is ready to do work.")
input("-- Press enter to continue --")
os.system("clear")
print("Suddenly out of nowhere, A 27 year old Japanese Lady named Karen Bakageta has walked up with a cart worth $1,592.99 of items. She proceeds to checkout when all of a sudden her card got declined ")
input("-- Press enter to continue --")
os.system("clear")
print("She demands to speak to the manager. Her son is crying because shes too broke to get the PlayStation16 which costed $162,251.99")
input("-- Press enter to continue --")
os.system("clear")
print("BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE! BOSS BATTLE!")
input("-- Press enter to continue --")
os.system("clear")

"Karen Bossfight"

options = ['Tell her to leave', "Gun", "Bomb"]

userInput = ''

inputMSG = "Pick a move: "

for index, item in enumerate(options):
    inputMSG += f'{index+1}) {item}\n'

inputMSG += 'Your choice: '

while userInput.lower() not in options:
    user_input = input(inputMSG)
    os.system("clear")
    input("Karen is immortal. Press enter to continue...")
    os.system("clear")