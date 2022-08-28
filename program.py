"""
Program to calculate win/loss ratio of games
"""

from ratioObject import *
from datetime import *

def menu():
    """
    prints out a menu of options that the user will later select out of
    """
    print("(0) Quit")
    print("(1) Display current win/loss ratios")
    print("(2) Add a win/loss ratio")
    print("(3) View history of a win/loss ratio")

def getChoice():
    """
    Gets user choice and validates inputs. Returns an integer corresponding to 
    an option on the menu
    """
    menu()
    choice = input("Please select one of the above options: ")
    while not choice.isdigit() or int(choice) < 0 or int(choice) > 3:
        menu()
        choice = input("Please select one of the above options: ")
    return int(choice)

def load():
    """
    Functions loads and processes file containing ratios
    """
    data=[]
    file = open("./ratios.txt")
    for line in file:
        data.append(line.strip().split(";;"))
    dataComp = []
    for i in range(len(data)):
        if not data[i][0] == "<GAME>":
            dataComp.append(ratObj(data[i][0],int(data[i][1]),int(data[i][2]),float(data[i][3]),data[i][4]))

    file.close()
    return dataComp

def display(data):
    """
    Function that displays all win/loss ratios
    """
    for item in data:
        print(item)

def addRat():
    """
    Function that adds a new ratio to data and loads data for display later
    """
    win = input("Enter the amount of wins: ")
    while not win.isdigit() or int(win) < 0:
        print("ERROR: Please enter a positive integer")
        win = input("Enter the number of wins: ")
    win = int(win)

    loss = input("Enter the amount of losses: ")
    while not loss.isdigit() or int(loss) < 0:
        print("ERROR: Please enter positive integer")
        loss = input("Enter the amount of losses: ")
    loss = int(loss)

    if win ==  0 and loss == 0:
        return
    else:
        ratio = win / (win + loss)

    game = input("What game is this ratio for? ")
    date = datetime.now()
    file = open("./ratios.txt", "a")
    file.write("\n" + "%s;;%s;;%s;;%s;;%s" % (game, win, loss, ratio, date))
    file.close()
    return load()

def history(data):
    game = input("For what game would you like to see your history of win/loss ratios? ")
    sum = 0
    count = 0
    for item in data:
        if item.getGame() == game:
            print(item)
            sum += item.getRatio()
            count += 1
    avg = sum / count
    print("Your overall average win-loss ratio is %f" % (avg))

def main():
    data = load()
    choice = 1
    while choice != 0:
        choice = getChoice()
        if choice == 1:
            display(data)
        elif choice == 2:
            data = addRat()
        elif choice == 3:
            history(data)

main()