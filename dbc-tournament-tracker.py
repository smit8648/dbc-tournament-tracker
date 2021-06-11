def getPlayerCount():
    flag = True
    while flag:
            
        player_count = input("How many players would you like in the tournament: ")
        if player_count.isnumeric() == False:
            print("please enter a numerical value")
        else:
            flag = False

    print(f"There are {player_count} players in the tournament")
    return (player_count)

##instantiate an empty list with however many players there are in the tournament

## !! Remove player_list instance below when trying to run menu (only for testing) !!



def addPlayer(player_list):
    flag = True
    while flag:
        playerName = input("Please enter the name of the player you'd like to add: ").title()
        playerPosition = int(input("Please enter the desired position of the player: "))

        if player_list[playerPosition-1] == None:
            player_list[playerPosition-1] = playerName
            flag = False
        else:
            print("sorry, that position is already filled.")
    return(player_list)


def removePlayer(player_list):
    flag = True
    while flag:
        playerName = input("Please enter the name of the player you'd like to remove: ").title()
        playerPosition = int(input("Please enter the desired position of the player you'd like to remove: "))

        if player_list[playerPosition-1] == playerName:
            player_list[playerPosition-1] = None
            flag = False
        else:
            print("sorry, that position is empty.")
    return(player_list)

def viewPlayers(player_list):
    for index, name in enumerate(player_list):
        print(index+1, name)
        




def menu():
    flag = True
    player_list = [None] * int(getPlayerCount())
    while flag:
        
        print("Hello, and welcome to the tournament creator. Here are your options: \n 1. Add Participant \n 2. Remove Participant \n 3. View Participant List \n 4. Exit Application")

        choice = int(input())
        if choice == 1:
            addPlayer(player_list)
        elif choice == 2:
            removePlayer(player_list)
        elif choice == 3:
            viewPlayers(player_list)
        elif choice == 4:
            exitChoice = input("are you sure you want to exit the application? (y/n)").lower()
            if exitChoice == "y" or exitChoice == "yes":
                flag = False
                SystemExit







