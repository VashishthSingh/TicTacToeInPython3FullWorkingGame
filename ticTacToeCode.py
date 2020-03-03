def show():
    for i in l:
        print(*i)

l=[['-','-','-'],['-','-','-'],['-','-','-']]
decider=0

def getPosition(pos):
    if pos==1 or pos==2 or pos==3:
        return(0)
    elif pos==4 or pos==5 or pos==6:
        return(1)
    else:
        return(2)

def getCorrectPosition(pos):
    if pos==1 or pos==2 or pos==3:
        return(pos-1)
    elif pos==4 or pos==5 or pos==6:
        return(pos-4)
    else:
        return(pos-7)

def winOrNot():
    flag=0
    for i in range(3):
        if l[i][0]=='0' and l[i][1]=='0' and l[i][2]=='0':
            flag=1
            break
    for j in range(3):
        if l[0][j]=='0' and l[1][j]=='0' and l[2][j]=='0':
            flag=1
            break
    for i in range(3):
        if l[i][0]=='X' and l[i][1]=='X' and l[i][2]=='X':
            flag=2
            break
    for j in range(3):
        if l[0][j]=='X' and l[1][j]=='X' and l[2][j]=='X':
            flag=2
            break
    if l[0][0]=='0' and l[1][1]=='0' and l[2][2]=='0':
        flag = 1
    elif l[0][2]=='0' and l[1][1]=='0' and l[2][0]=='0':
        flag=1
    if l[0][0]=='X' and l[1][1]=='X' and l[2][2]=='X':
        flag = 2
    elif l[0][2]=='X' and l[1][1]=='X' and l[2][0]=='X':
        flag=2
    return(flag)

def startGame():
    global decider
    global endGame
    if decider==0:
        while True:
            try:
                playerOne=int(input("Enter position player ONE : "))
                if playerOne>0 and playerOne<10:
                    break
                else:
                    print("Invalid Input, Position Must Range Between 1-9 Only")
            except:
                print("Invalid Input Position Must Range Between 1-9 Only")

        position=getPosition(playerOne)
        playerOne=getCorrectPosition(playerOne)
        decider = 1
        if l[position][playerOne]=='-':
            l[position][playerOne]='0'
            player=winOrNot();
            if player==1:
                print("Player One Won The Game")
                endGame=1
            elif player==2:
                print("Player Two Won The Game")
                endGame=1
        else:
            print("Invalid Position already inserted")
            decider=0
        show()
    else:
        while True:
            try:
                playerTwo=int(input("Enter position player TWO: "))
                if playerTwo>0 and playerTwo<10:
                    break
                else:
                    print("Invalid Input, Position Must Range Between 1-9 Only")
            except:
                print("Invalid Input Position Must Range Between 1-9 Only")
        position=getPosition(playerTwo)
        playerTwo=getCorrectPosition(playerTwo)
        decider = 0
        if l[position][playerTwo]=='-':
            l[position][playerTwo] = 'X'
            player = winOrNot();
            if player==1:
                print("Player One Won The Game")
                endGame = 1
            elif player==2:
                print("Player Two Won The Game")
                endGame = 1
        else:
            print("Invalid Position already inserted")
            decider=1
        show()

endGame=0
gameDraw=0
while(True):
    if endGame!=1:
        startGame()
    gameDraw+=1
    if endGame==1:
        print("Play Again Y/N : ")
        playAgain=input()
        if playAgain=='Y' or playAgain=='y':
            endGame=0
            for i in range(3):
                for j in range(3):
                    l[i][j]='-'
            decider=0
            endGame = 0
            gameDraw = 0
        else:
            break
    if(gameDraw==9 and endGame!=1):
        print("Game Draw")
        endGame=1

