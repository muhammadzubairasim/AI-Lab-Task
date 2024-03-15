def getIntNumber(str):
    while True:
        try:
            return int(input(str))
        except ValueError:
            print("Wrong Input Enter Correct Input in Integer")
def ValidateInt(val):
    try:
        val = int(val)
        return True
    except ValueError:
        return False
def PlayerListGenerator(num):
    playerName = []
    for i in range(0,num):
        playerName.append(input(f"Enter Name of {i}th Player"))
    return playerName
def ContinueGame():
    global sequence
    sequence+=1
    PrintTll(sequence)
def PrintTll(num):
    for i in range(1,num+1):
        if(i%3==0 and i%5==0):
            print("Fizz buzz")
        elif i%5==0:
            print("buzz")
        elif i%3==0:
            print("fizz")
        else:
            print(i)

gameRound = getIntNumber("Enter Number of Rounds you want to play ")
playersCount = getIntNumber("Enter Number of players you want to play ")
sequence = 0
playerListFinal = PlayerListGenerator(playersCount)

for i in range(0,gameRound):
    playerList = playerListFinal[:]
    sequence = 0
    print(f"Round {i+1} Started ")
    while len(playerList) > 0:
        for j in playerList:
            player = input(f'Player {j} turn : ')
            if (player.lower() == "fizz" and (sequence+1)%3 == 0) or ((sequence+1)%5 == 0 and (sequence+1)%3==0 and player.lower() == "fizz buzz") or ((sequence+1)%5 == 0 and player.lower() == "buzz"):
                ContinueGame()
            elif ValidateInt(player) and (int(player) == sequence +1 and int(player)%3!=0 and int(player)%5!=0):
                ContinueGame()
            else:
                print(f'player {j} lose ')
                playerList.remove(j)
    print("\n")