import random
import Network_base_class as networkClass
import Base_evolution_software as evo

def GenerateRandomNumber(lower, upper):
    number = random.randint(lower, upper)
    return number


def saveNetwork(network, difficulty, savelist):
    
    ## Format of savelist : [[net, diff], [net, diff]...]
    
    done = False
    
    while done == False:
        print ("")
        choice = input("Pick a place to save the network (1,2 or 3): ")
        if choice == "1" or choice == "2" or choice == "3":
            choice = int(choice)
            index = choice - 1
            done = True
        else:
            print ("")
            print ("Please enter a valid save slot")
            
    done = False
            
    if savelist[index][0] != None:
        print ("")
        print ("Saving this network in slot {0} will overwrite the {1} network already there".format(choice, savelist[index][1]))
        while done == False:
            choice2 = input("Would you like to procede (y or n): ")
            if choice2 == "y" or choice2 == "n":
                done = True
            else:
                print ("Please enter either y or n")
        if choice2 == "y":
            print ("Network successfully saved at position {0}".format(choice))
            savelist[index][0] = network
            savelist[index][1] = difficulty
        elif choice2 == "n":
            print ("New network not saved, previous network intact")
    
    else:
        savelist[index][0] = network
        savelist[index][1] = difficulty
        print ("Network successfully saved")
        
        return savelist


class Board:

    def __init__(self, won):
        self.won = False
        self.values = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]

    def returnBoardState(self):
        state = self.values
        return state

    def changeBoard(self, choice, turnCounter, playerList):
        playerTurn = (turnCounter) % 2
        currentPlayer = playerList[playerTurn]

        index1 = (choice - 1) // 3
        index2 = (choice - 1) % 3

        validChoice = False
        if self.values[index1][index2] == " ":
            self.values[index1][index2] = currentPlayer
            validChoice = True
            return validChoice
        else:
            print ("That space has been taken! Choose an empty square")
            return validChoice
                

    def displayBoard(self, turnCounter, playerList): # turnCounter will be function called in
        ## Put turnCounter and playerList back in -- Done
        playerTurn = (turnCounter) % 2
        currentPlayer = playerList[playerTurn]

        print ("")
        print ("")

        print ("Player {0} ({1}) goes:".format(playerTurn + 1, currentPlayer))
        
        print ("")
        print ("")
        
        print ('''Squares are numbered like this:
1|2|3
4|5|6
7|8|9 ''')

        print ("")
        print ("")

        print ("The current game board:")

        print ("")
        print ("")

        ## Need code to print game board itself -- Done

        print (''' {0} | {1} | {2}
-----------
 {3} | {4} | {5}
-----------
 {6} | {7} | {8}'''.format(self.values[0][0], self.values[0][1], self.values[0][2], self.values[1][0], self.values[1][1], self.values[1][2], self.values[2][0], self.values[2][1], self.values[2][2]))


    def displayFinalBoard(self):

        print (''' {0} | {1} | {2}
-----------
 {3} | {4} | {5}
-----------
 {6} | {7} | {8}'''.format(self.values[0][0], self.values[0][1], self.values[0][2], self.values[1][0], self.values[1][1], self.values[1][2], self.values[2][0], self.values[2][1], self.values[2][2]))        


    def checkBoard(self, choice, turnCounter, playerList):
        vw = []
        hw = []
        dwr = []
        dwl = []
        win = None
        notDraw = False

        playerTurn = (turnCounter) % 2
        currentPlayer = playerList[playerTurn]
        
        index3 = (choice - 1) // 3
        index4 = (choice - 1) % 3

        ## Check for vertical win -- works

        checkList = []
        for x in range(0,3):
            character = self.values[x][index4]
            if character == currentPlayer:
                checkList.append(character)
                vw.append("VW")
        if len(checkList) == 3:
            win = currentPlayer
            notDraw = True
            

        ## Check for horizontal win -- works

        counter = 0
        checkList = []
        for character in self.values[index3]:
            if character == currentPlayer:
                checkList.append(character)
                hw.append("HW")
            counter += 1
        if len(checkList) == 3:
            win = currentPlayer
            notDraw = True
            

        ## Check for diagonal win right -- works

        if choice == 1 or choice == 3 or choice == 5 or choice == 7 or choice == 9:

            counter = 0
            checkList = []
            for x in range(0,3):
                character = self.values[x][x]
                if character == currentPlayer:
                    checkList.append(character)
                    dwr.append("DWR")
                counter += 1
            if len(checkList) == 3:
                win = currentPlayer
                notDraw = True
                

            ## Check for diagonal win left -- works

            checkList = []
            for x1 in range(0,3):
                x2 = 2 - x1
                character = self.values[x1][x2]
                if character == currentPlayer:
                    checkList.append(character)
                    dwl.append("DWL")
            if len(checkList) == 3:
                win = currentPlayer
                notDraw = True
                

        ## Check for draw -- works

        checkList = []
        for array in self.values:
            for character in array:
                if character == ' ':
                    break
                else:
                    checkList.append('Taken')
        if len(checkList) == 9:
            if notDraw == False:
                win = 'draw'
            

        if win == None:
            win = False
        
        finalOutput = []
        finalOutput.append(win)
        finalOutput.append(vw)
        finalOutput.append(hw)
        finalOutput.append(dwr)
        finalOutput.append(dwl)

        ## Order of output:
        ## 0: win
        ## 1: number of consecutive verticals
        ## 2: number of consecutive horizontals
        ## 3: number of right diagonal squares
        ## 4: number of left diagonal squares
        
        return finalOutput
        

class HumanPlayer:
    def __init__(self):
        pass

    def coinToss(self):
        
        ## Heads or tails to decide first turn

        coinDone = False
        while coinDone == False:
            coinChoice = input ("Choose heads or tails: h or t: ")
            print ("")
            if coinChoice == 'h' or coinChoice == 'H':
                coinDone = True
                coinChoice = 'h'
            if coinChoice == 't' or coinChoice == 'T':
                coinDone = True
                coinChoice = 't'
            else:
                print ("Please ensure you have correctly entered you choice")
                print ("")
                
        ## Needs data validation -- Done
                
        coinFlip = GenerateRandomNumber(0,100)

        coinCounter = False
        while coinCounter == False:
            if coinFlip < 50:
                coinResult = 'h'
                coinCounter = True
            elif coinFlip > 50:
                coinResult = 't'
                coinCounter = True
            elif coinFlip == 50:
                GenerateRandomNumber(0, 100)

        if coinChoice == coinResult:
            print ("You guessed right! You can go first!")
            right = True

        else:
            print ("Unlucky, you guessed wrong! The other player will go first")
            right = False

        return right 
        
    def assignHumanPlayer(self):
        
        ## Team selection input from player + data validation
                
        teamSelectionCounter = 1
        while teamSelectionCounter == 1:
            humanPlayer = input ("Choose a team to play as: X or O: ")
            if humanPlayer != 'X' and humanPlayer != 'x' and humanPlayer != 'O' and humanPlayer != 'o':
                print ("Please either select 'X' or 'O'")
            else:
                teamSelectionCounter += 1

        ## Assignment of players to teams
        ## Human player is list index 0, player 2 is list index 1

        if humanPlayer == 'X' or humanPlayer == 'x':
            playerList = ['X', 'O']
        elif humanPlayer == 'O' or humanPlayer == 'o':
            playerList = ['O', 'X']

        return playerList


def turnCounter(right):
    if right == True:
        turnCounter = 0
    if right == False:
        turnCounter = 1

    return turnCounter

def nextPlayerMove():

    validChoice = False
    validCharacter = False
    while validChoice == False:
        while validCharacter == False:
            try:
                validCharacter = True
                moveChoice = int (input ("Enter the number of the square you would like to go in (1-9): "))
            except ValueError:
                print ("Please enter a number between 1 and 9; try again")
                validCharacter = False

        while validChoice == False:  
            if moveChoice > 9 or moveChoice < 1:
                ### ERROR HERE - Infinite loop - need to fix -- resolved
                print ("Please enter a number between 1 and 9; try again")
                print ("")
                moveChoice = int (input ("Enter the number of the square you would like to go in (1-9): "))
            else:
                validChoice = True
            
        
    ## ^^ Needs data validation
    return moveChoice    


def displayWinner(win, turnCounter, flag):

    if flag == True:

        playerTurn = (turnCounter) % 2

        print ("")
        print ("")

        print ("Player {0} ({1}) wins!".format(playerTurn + 1, win))


def displayDraw(win, flag):

    if flag == True:

        print ("")
        print ("")

        print ("The game is a {0}!".format(win))

## Random AI function -----------------------------------------------------------------------------------------

def randomAIMove():
        RAIChoice = GenerateRandomNumber(0,9)
        return RAIChoice

## -------------------------------------------------------------------------------------------------------------

## Game menu function ------------------------------------------------------------------------------------------

def primaryMenu():

    firstValid = False
    while firstValid == False:
    
        print ("Would you like to play a game for two people?")
        playerNumberChoice = input ("Make your choice (yes or no): ")

        if playerNumberChoice == "yes" or playerNumberChoice == "Yes":

            firstValid = True
            
            ## This will take the player to the standard two player game
            
            opponent = 'human'
            
        elif playerNumberChoice == "no" or playerNumberChoice == "No":
            
            ## This takes the player to the next menu
            
            secondValid = False
            
            while secondValid == False:
                print ("Would you like to play a game against a random AI, a basic AI, or a trained neural network?")
                print ("")
                playerOpponentChoice = input ("Make your choice - type 1 for a random AI, 2 for a basic AI, and 3 for a neural network: ")
                if playerOpponentChoice == "1" or playerOpponentChoice == "2" or playerOpponentChoice == "3":
                    playerOpponentChoice = int (playerOpponentChoice)
                print ("")
    
                if playerOpponentChoice == 1:
                    opponent = 'random'
                    print ("You have chosen {0}!".format(opponent))
                    print ("")
                    firstValid = True
                    secondValid = True
                elif playerOpponentChoice == 2:
                    opponent = 'basic'
                    print ("You have chosen {0}!".format(opponent))
                    print ("")
                    firstValid = True
                    secondValid = True
                elif playerOpponentChoice == 3:
                    opponent = 'network'
                    print ("You have chosen {0}!".format(opponent))
                    print ("")
                    firstValid = True
                    secondValid = True
                else:
                    print ("Please select a valid option")
                    print ("")
            
        else:
            print ("Be sure you have entered your decision correctly")
            print ("")
            
    return opponent

## Function that checks for game win ------------------------------------------------------

## SERIOUS ISSUES BELOW -- resolved

def mainGameChecker(turn, board, choice, playerlist, disFlag, flag):  
        checker = board.checkBoard(choice, turn, playerlist)
        if checker[0] == False:
            pass
        elif checker[0] == 'draw':
            displayDraw(checker[0], flag)
            if disFlag == True:
                board.displayFinalBoard()
            board.won = True
        else:
            displayWinner(checker[0], turn, flag)
            if disFlag == True:
                board.displayFinalBoard()
            board.won = True
        turn += 1
        return turn

## ---------------------------------------------------------------------------------------------------------------

## Random AI move function -----------------------------------------------
    
def randomAITurn(turn, gameBoard, playerListMain, disFlag, flag):
    
    RAIChoice = randomAIMove()
    RAIIndex1 = (RAIChoice - 1) // 3
    RAIIndex2 = (RAIChoice - 1) % 3
    RAIDone = False
    boardState = gameBoard.returnBoardState()

    while RAIDone == False:
        if boardState[RAIIndex1][RAIIndex2] == " ":
            gameBoard.changeBoard(RAIChoice, turn, playerListMain)
            RAIDone = True
        else:
            RAIChoice = randomAIMove()
            RAIIndex1 = (RAIChoice - 1) // 3
            RAIIndex2 = (RAIChoice - 1) % 3

    turn = mainGameChecker(turn, gameBoard, RAIChoice, playerListMain, disFlag, flag)
    return turn, RAIChoice

## ----------------------------------------------------------------

## Basic AI move function -----------------------------------------

def basicAITurn(turn, gameBoard, choice, playerListMain, endBoardState, disFlag, flag):

    boardState = gameBoard.returnBoardState()
    
    playerMove = choice
    playerIndex1 = (playerMove - 1) // 3
    playerIndex2 = (playerMove - 1) % 3

    diagRightCounter = []
    diagLeftCounter = []
    
    ## Order of output:
    ## 0: win
    ## 1: number of consecutive verticals
    ## 2: number of consecutive horizontals
    ## 3: number of right diagonal squares
    ## 4: number of left diagonal squares

    ## Check to see if there are any winning combinations on the board
    
    hcperm = []
    
    for x1 in range(0,3):
        row = boardState[x1]
        horizontalCounter = []
        for x2 in range(0,3):
            if row[x2] == playerListMain[1]:
                horizontalCounter.append("HC")
                ## print (horizontalCounter)
                if len(horizontalCounter) == 2:
                    x1perm = x1
                    hcperm = horizontalCounter
                    ## print (hcperm) -- just a test
            elif row[x2] == playerListMain[0]:
                horizontalCounter.append("sabotage")
                horizontalCounter.append("sabotage")
                horizontalCounter.append("sabotage")

                ## ^^This prevents the AI from picking a line of two friendly icons and an enemy icon
                
    for x2 in range(0,3):
        verticalCounter = []
        for x1 in range(0,3):
            if boardState[x1][x2] == playerListMain[1]:
                verticalCounter.append("VC")
                ## print (verticalCounter)
                if len(verticalCounter) == 2:
                    x2perm = x2
            elif boardState[x1][x2] == playerListMain[0]:
                verticalCounter.append("sabotage")
                verticalCounter.append("sabotage")
                verticalCounter.append("sabotage")

    for x in range(0,3):
        character = boardState[x][x]
        if character == playerListMain[1]:
            diagRightCounter.append("DRC")
        elif character == playerListMain[0]:
            diagRightCounter.append("sabotage")
            diagRightCounter.append("sabotage")
            diagRightCounter.append("sabotage")

    for xld1 in range(0,3):
        xld2 = 2 - xld1
        character = boardState[xld1][xld2]
        if character == playerListMain[1]:
            diagLeftCounter.append("DLC")
        elif character == playerListMain[0]:
            diagLeftCounter.append("sabotage")
            diagLeftCounter.append("sabotage")
            diagLeftCounter.append("sabotage")

    blockDone = False
                
    if len(hcperm) == 2:
        ## print ("HCHECK")
        row = boardState[x1perm]
        for x in range(0,3):
            if row[x] == " ":
                BAIChoice = (3 * x1perm) + x + 1

    elif len(verticalCounter) == 2:
        # print ("VCHECK")
        for x in range(0,3):
            character = boardState[x][x2perm]
            if character == " ":
                BAIChoice = (3 * x) + x2perm + 1
                
    elif len(diagRightCounter) == 2:
        # print ("DRCHECK")
        for x in range(0,3):
            character = boardState[x][x]
            if character == " ":
                BAIChoice = (4 * x) + 1
                
    elif len(diagLeftCounter) == 2:
        # print ("DLCHECK")
        for xld1 in range(0,3):
            xld2 = 2 - xld1
            character = boardState[xld1][xld2]
            if character == " ":
                BAIChoice = (3 * xld1) + xld2 + 1

    ## If no winning move can be found, try to find a blocking move

    else:
        ## print (endBoardState)
        if len(endBoardState[1]) == 2:
            ## print ("BV")
            for x in range(0,3):
                character = boardState[x][playerIndex2]
                if character == " ":
                    BAIChoice = (3 * x) + playerIndex2 + 1
                    blockDone = True
        elif len(endBoardState[2]) == 2:
            ## print ("BH")
            for x in range(0,3):
                character = boardState[playerIndex1][x]
                if character == " ":
                    BAIChoice = (3 * playerIndex1) + x + 1
                    blockDone = True
        elif len(endBoardState[3]) == 2:
            ## print ("BDR")
            for x in range(0,3):
                character = boardState[x][x]
                if character == " ":
                    BAIChoice = (4 * x) + 1
                    blockDone = True
        elif len(endBoardState[4]) == 2:
            ## print ("BDL")
            for x1 in range(0,3):
                x2 = 2 - x1
                character = boardState[x1][x2]
                if character == " ":
                    BAIChoice = (3 * x1) + x2 + 1
                    blockDone = True
                    
        BAIDone = False
        if blockDone == False:
            while BAIDone == False:
                ## print ("CHECK FINAL")
                BAIChoice = randomAIMove()
                BAIRow = (BAIChoice - 1) // 3
                BAIColumn = (BAIChoice - 1) % 3
                if boardState[BAIRow][BAIColumn] == " ":
                    BAIDone = True
                else:
                    pass

    ## print (BAIChoice)
    
    gameBoard.changeBoard(BAIChoice, turn, playerListMain)
    
    turn = mainGameChecker(turn, gameBoard, BAIChoice, playerListMain, disFlag, flag)
    
    return turn, BAIChoice

## ----------------------------------------------------------------

## Network turn ---------------------------------------------------

def makeNetworkDecision(turn, gameBoard, outputLayer, playerListMain, disFlag, flag):

    stateList = []
    state = gameBoard.returnBoardState()
    for x1 in range (0,3):
        for x2 in range(0,3):
            stateList.append(state[x1][x2])
    ## print (stateList)

    ## [[0.756, 3], [0.997, 1], [0.523, 7] ... ]
    ## [0.756, 0.997, 0.523, ... ]

    done = False
    outputList = list(outputLayer)

    while done == False:
        nodeIndex = outputList.index(max(outputList)) + 1
        ## print (nodeIndex)
        if stateList[nodeIndex - 1] == " ":
            done = True
        else:
            outputList[nodeIndex - 1] = 0

    ## print (nodeIndex)
    gameBoard.changeBoard(nodeIndex, turn, playerListMain)

    turn = mainGameChecker(turn, gameBoard, nodeIndex, playerListMain, disFlag, flag)
    return turn, nodeIndex

## ----------------------------------------------------------------

## AUTOPLAY FUNCTION AREA -----------------------------------------

def autoplay(opponent, repeats, net):
    ## opponent will be either random or basic ai
    ## new network will take the place of the human player (will always be turn 0)
    done1 = False
    while done1 == False:
        number = GenerateRandomNumber(-1,1)
        if number < 0:
            turn = 0
            done1 = True
        elif number > 0:
            turn = 1
            done1 = True
        else:
            pass
        
    done2 = False
    while done2 == False:
        number = GenerateRandomNumber(-1,1)
        if number < 0:
            playerListMain = ['X', 'O']
            done2 = True
        elif number > 0:
            playerListMain = ['O', 'X']
            done2 = True
        else:
            pass
    
        ## The loops will both continue if exactly 0 is thrown
        
    mainCounter = 0
    winList = []
    
    while mainCounter <= repeats:
        
        gameBoard = Board(False)
        while gameBoard.won == False:
            ## print ('stuck')
            
            boardState = gameBoard.returnBoardState()
            ## print (boardState)
            
            if turn % 2 == 0:
                
                boardStateAdjusted = []
                for x in range(0,3):
                    for item in boardState[x]:
                        ## print ('check')
                        if item == playerListMain[turn % 2]:
                            boardStateAdjusted.append(0.9990)
                        elif item == playerListMain[(turn + 1) % 2]:
                            boardStateAdjusted.append(0.0010)
                        else:
                            boardStateAdjusted.append(0.5000)
                    
                outputLayer = net.feedForward(boardStateAdjusted)
                final = makeNetworkDecision(turn, gameBoard, outputLayer, playerListMain, False, False)
                choice = final[1]
                endBoardState = gameBoard.checkBoard(choice, turn, playerListMain)
                win = endBoardState[0]
                turn = final[0]
                if gameBoard.won == True:
                    if win != 'draw':
                        winList.append((turn-1) % 2)
                    else:
                        winList.append('-')
            elif turn % 2 == 1:
                
                if opponent == 'random':
                    final = randomAITurn(turn, gameBoard, playerListMain, False, False)
                    turn = final[0]
                    choice = final[1]
                    
                elif opponent == 'basic':
                    if turn == 1:
                            
                        final = randomAITurn(turn, gameBoard, playerListMain, False, False)
                        turn = final[0]
                        choice = final[1]
                                    
                    else:

                        final = basicAITurn(turn, gameBoard, choice, playerListMain, endBoardState, False, False)
                        turn = final[0]
                        choice = final[1]
                
                endBoardState = gameBoard.checkBoard(choice, turn, playerListMain)
                win = endBoardState[0]
                if gameBoard.won == True:
                    if win != 'draw':
                        winList.append((turn-1) % 2)
                    else:
                        winList.append('-')
        mainCounter += 1
    return winList
        

## ----------------------------------------------------------------

## MAIN GAME LOOP ------------------ Don't touch ------------------

def run():
    
    playAgain = True
    network_ = False
    saveList = [[None, None], [None, None], [None, None]] ## Could eventually be fed in as an external file

    while playAgain == True:

        opponentChoice = primaryMenu()

        gameBoard = Board(False)
        humanPlayer = HumanPlayer()
        playerListMain = humanPlayer.assignHumanPlayer()

        ## These statements will take the player to the correct game mode

        
        if opponentChoice == 'human':
            
            turn = turnCounter(humanPlayer.coinToss())
            
            while gameBoard.won == False:
                
                gameBoard.displayBoard(turn, playerListMain)
                choice = nextPlayerMove()
                
                valid = False
                while valid == False:
                    
                    valid = gameBoard.changeBoard(choice, turn, playerListMain)
                    if valid == True:
                        pass
                    elif valid == False:
                        choice = nextPlayerMove()
                        valid = gameBoard.changeBoard(choice, turn, playerListMain)
                turn = mainGameChecker(turn, gameBoard, choice, playerListMain, True, True)
                
                    
        elif opponentChoice == 'random':

            ## This will be the AI's turn

            coinRight = turnCounter(humanPlayer.coinToss())
            if coinRight == False:
                turn = 1
            elif coinRight == True:
                turn = 0
            
            while gameBoard.won == False:
                gameBoard.displayBoard(turn, playerListMain)
                if turn % 2 == 1:
                    
                    turn = randomAITurn(turn, gameBoard, playerListMain, True, True)[0]

                elif turn % 2 == 0:
                    
                    ## This will be the human player's turn
                    
                    choice = nextPlayerMove()
                    
                    valid = False
                    while valid == False:
                        valid = gameBoard.changeBoard(choice, turn, playerListMain)
                        if valid == True:
                            pass
                        elif valid == False:
                            choice = nextPlayerMove()
                            valid = gameBoard.changeBoard(choice, turn, playerListMain)
                    turn = mainGameChecker(turn, gameBoard, choice, playerListMain, True, True)
                
            
        elif opponentChoice == 'basic':
                
                coinRight = humanPlayer.coinToss()
                if coinRight == False:
                    turn = 1
                elif coinRight == True:
                    turn = 0
                
                while gameBoard.won == False:
                    
                    BAIDone = False
                    boardState = gameBoard.returnBoardState()
                    gameBoard.displayBoard(turn, playerListMain)
                    
                    if turn % 2 == 1:
                        
                        if turn == 1:
                            
                            turn = randomAITurn(turn, gameBoard, playerListMain, True, True)[0]
                                    
                        else:

                            turn = basicAITurn(turn, gameBoard, choice, playerListMain, endBoardState, True, True)[0]

                    elif turn % 2 == 0:
                        
                        ## This will be the human player's turn
                        
                        choice = nextPlayerMove()
                        valid = False
                        while valid == False:
                            valid = gameBoard.changeBoard(choice, turn, playerListMain)
                            if valid == True:
                                pass
                            elif valid == False:
                                choice = nextPlayerMove()
                                valid = gameBoard.changeBoard(choice, turn, playerListMain)
                        endBoardState = gameBoard.checkBoard(choice, turn, playerListMain)
                        ## print (endBoardState)
                        turn = mainGameChecker(turn, gameBoard, choice, playerListMain, True, True)

        
        elif opponentChoice == 'network':
            
            network_ = True
            difficulty = None
            
            new = False
            old = False
            
            
            checker = 0
            for item in saveList:
                if item[0] != None:
                    checker += 1
                
            if checker == 0:
                new = True
                old = False
                
            else:
            
                done = False
            
                while done == False:
                    print ("")
                    mainChoice = input("Would you like to play against a new neural network, or a saved one (new or old): ")
                    if mainChoice == "new" or mainChoice == "old":
                        done = True
                    else:
                        print ("")
                        print ("Please type either new or old")
                
                if mainChoice == "new":
                    new = True
                    old = False
                elif mainChoice == "old":
                    new = False
                    old = True
                    
            if new == True:
            
                print ("")
                print ("Would you like to play an easy, average or skilled neural network?")
                print ("")
                print ("Warning: more skilled networks will take longer to evolve")
                print ("Due to the randomness of evolution, eventual difficulty of networks cannot be guaranteed")
                print ("")
                
                done = False
                while done == False:
                    difficulty = input("Choose 1 for easy, 2 for average, 3 for skilled or 4 for extreme: ")
                    if difficulty == "1" or difficulty == "2" or difficulty == "3" or difficulty == "4":
                        difficulty = int(difficulty)
                        done = True
                    else:
                        print ("Please enter a valid option")
                        print ("")
                        
                if difficulty == 1:
                    difficulty = "easy"
                    net = evo.speciesTimeline(100, 10, 100, 0.5)[1]
                elif difficulty == 2:
                    difficulty = "average"
                    net = evo.speciesTimeline(100, 10, 300, 0.5)[1]
                elif difficulty == 3:
                    difficulty = "skilled"
                    net = evo.speciesTimeline(100, 10, 450, 0.5)[1]
                elif difficulty == 4:
                    difficulty = "extreme"
                    net = evo.speciesTimeline(100, 10, 1000, 0.5)[1]
                    
            elif old == True:
                
                print ("Here is the list of saved networks:")
                print (saveList)
                
                done = False
                
                while done == False:
                    print ("")
                    slot = input("Select a memory slot (1-3): ")
                    if slot == "1" or slot == "2" or slot == "3":
                        slot = int(slot)
                        slot = slot - 1
                        if saveList[slot][0] != None:
                            net = saveList[slot][0]
                            difficulty = saveList[slot][1]
                            done = True
                        else:
                            print ("")
                            print ("Please select a slot that houses a network")
                    else:
                        print ("")
                        print ("Please select a number between 1 and 3")

            coinRight = humanPlayer.coinToss()
            if coinRight == False:
                turn = 1
            elif coinRight == True:
                turn = 0
            
            while gameBoard.won == False:
                
                boardState = gameBoard.returnBoardState()
                gameBoard.displayBoard(turn, playerListMain)
                
                if turn % 2 == 1:

                    boardStateAdjusted = []
                    for x in range(0,3):
                        for item in boardState[x]:
                            if item == playerListMain[turn % 2]:
                                boardStateAdjusted.append(0.9990)
                            elif item == playerListMain[(turn + 1) % 2]:
                                boardStateAdjusted.append(0.0010)
                            else:
                                boardStateAdjusted.append(0.5000)
                    
                    outputLayer = net.feedForward(boardStateAdjusted)
                    turn = makeNetworkDecision(turn, gameBoard, outputLayer, playerListMain, True, True)[0]
                    

                elif turn % 2 == 0:
                    
                    ## This will be the human player's turn
                    
                    choice = nextPlayerMove()
                    valid = False
                    while valid == False:
                        valid = gameBoard.changeBoard(choice, turn, playerListMain)
                        if valid == True:
                            pass
                        elif valid == False:
                            choice = nextPlayerMove()
                            valid = gameBoard.changeBoard(choice, turn, playerListMain)
                    endBoardState = gameBoard.checkBoard(choice, turn, playerListMain)
                    ## print (endBoardState)
                    turn = mainGameChecker(turn, gameBoard, choice, playerListMain, True, True)
                    

            ## VITAL -- game repeat code will be used in every game mode
        
        if gameBoard.won == True:
            if network_ == True:
                done = False
                while done == False:
                    savenetwork = input("Would you like to play against this network again this session? (y or n): ")
                    if savenetwork == "y":
                        saveNetwork(net, difficulty, saveList)
                        done = True
                    elif savenetwork == "n":
                        print ("Network not saved")
                        done = True
                    else:
                        print ("Please select a valid option")
            validAgain = False
            while validAgain == False:
                playAgain = input ("Play again? Yes or no: ")
                if playAgain == 'yes' or playAgain == 'Yes':
                    playAgain = True
                    validAgain = True
                    gameBoard.won = False

                    print ("")
                    print ("")

                    print ("New game starting now")
                        
                elif playAgain == 'no' or playAgain == 'No':
                    playAgain = False
                    validAgain = True

                    print ("")
                    print ("")
                    
                    ## saveList could be saved to an external file at this point

                    print ("Ok, see you next time")

if __name__ == "__main__":
    run()


## Need to fix last-square win -- fully resolved
## Need further checks to see if the AI picks winning moves every time -- fully resolved
## Need major checks of blocking system as doesn't seem to work at all -- fully resolved
