"""
CMPT310: a4.py
Eric Huang
"""
import random
import copy #For deepcopy in AIMove()
import operator #For finding max in a dictionary in AIMove()

class TicTacToe:
    def __init__(self, boardState):
        self.boardState = boardState

    def setBoardState(self, boardState):
        self.boardState = boardState

    def convert(num):
        """Helper Function for drawBoard()"""
        if (num == 0): return "   "
        elif (num == 1 ): return " O "
        else: return " X "

    def drawBoard(self):
        boardState = self.boardState
        horizontalBar = "-----------"
        for i in range(3):
            print("%s|%s|%s" %(TicTacToe.convert(boardState[i*3]),
                TicTacToe.convert(boardState[i*3+1]), TicTacToe.convert(boardState[i*3+2])))
            if (i != 2):    #don't print the bar on the last line
                print(horizontalBar)

    def move(self, player, place):
        """Places the player's token in the place specified if the place is empty.
        Returns true if move is legal, false otherwise."""
        if (place > len(self.boardState)):
            #Place outside of grid. (illegal move)
            return False
        elif (self.boardState[place] != 0):
            #Place is already occupied. (illegal move)
            return False
        else:
            self.boardState[place] = player
            return True

    def checkWin(self, player):
        """Used at game runtime for checking which player won.
        Returns True if a player has won, False otherwise."""
        board = self.boardState
        victoryMsg = "Player %d Won!" %(player)
        #Horizontal Win
        for i in range(3):
            if (board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != 0):
                print(victoryMsg)
                return True
        #Vertical Win
        for i in range(3):
            if (board[i] == board[i+3] == board[i+6] and board[i] != 0):
                print(victoryMsg)
                return True
        #Diagonal Win
        if (board[0] == board[4] == board[8] and board[0] != 0):
            print(victoryMsg)
            return True
        if (board[2] == board[4] == board[6] and board[2] != 0):
            print(victoryMsg)
            return True
        #Ties
        if (board.count(0) == 0):
            print("Tie Game.")
            return True
        #Game still not decided yet
        else: return False

    def checkCompWin(self):
        """Used by AI to determine the game outcome when deciding moves.
        Returns 0 if game is not over yet, 1 on AI wins, 2 on AI losses, and 3 on tie games."""
        board = self.boardState
        AI = 2  #Computer's Player Token
        #Horizontal
        for i in range(3):
            if (board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != 0):
                if (board[i*3] == AI):
                    return 1
                else: return 2
        #Vertical
        for i in range(3):
            if (board[i] == board[i+3] == board[i+6] and board[i] != 0):
                if(board[i] == AI):
                    return 1
                else: return 2
        #Diagonal
        if (board[0] == board[4] == board[8] and board[0] != 0):
            if (board[0] == AI):
                return 1
            else: return 2
        elif (board[2] == board[4] == board[6] and board[2] != 0):
            if (board[2] == AI):
                return 1
            else: return 2
        #Ties
        if (board.count(0) == 0):
            return 3
        #Game still not decided yet
        else: return 0

def AIMove(game):
    """Computer makes its move using Monte-Carlo Tree Search"""
    #Make a list of all legal moves
    legalMoves = {}
    movesArr = []
    for i in range(len(game.boardState)):
        if (game.boardState[i] == 0):
            legalMoves[i] = 0
            movesArr.append(i)

    humanToken = 1
    AIToken = 2
    numPlayouts = 2500
    win = 5
    tie = 4
    lose = -5
    #Do random playouts for each of the legal moves to determine the optimal move
    for move in legalMoves:
        #print("-----------MOVE: %d---------" %(move))
        copyGame = copy.deepcopy(game)
        copyGame.move(AIToken, move)
        copyMoves = copy.deepcopy(movesArr)
        copyMoves.remove(move)

        for i in range(0, numPlayouts):
            randomGame = copy.deepcopy(copyGame)
            randomMoves = copy.deepcopy(copyMoves)
            testGameOver = False
            turn = 1
            while (testGameOver == False and len(randomMoves) > 0):
                if (turn % 2 == 1):
                    #random human move
                    randomHuman = random.choice(randomMoves)
                    randomGame.move(humanToken, randomHuman)
                    randomMoves.remove(randomHuman)
                else:
                    #random AI move
                    randomAI = random.choice(randomMoves)
                    randomGame.move(AIToken, randomAI)
                    randomMoves.remove(randomAI)

                #check if game is over
                gameState = randomGame.checkCompWin()
                #print("gameState: %d" %(gameState))
                #randomGame.drawBoard()
                if (gameState == 0):  #game not over yet
                    turn += 1
                else:
                    #Update values of move
                    if (gameState == 1): legalMoves[move] += win
                    elif (gameState == 2): legalMoves[move] += lose
                    else: legalMoves[move] += tie
                    testGameOver = True
                    break

    #Choose the optimal move
    bestMove = max(legalMoves.items(), key=operator.itemgetter(1))[0]
    game.move(AIToken, bestMove)
    #print(legalMoves)
    #print("bestMove: ", bestMove)
    return

def askPlayerForMove(game, player):
    while (True):
        place = input("Player %d's Turn: " %(player))
        if (game.move(player, int(place)) == True):
            return
        else:
            print("Sorry, that was an illegal move. Please try again.")

def game():
    """TicTacToe Game"""
    #Instructions
    print("Instructions: ")
    print("The game board has indexes as follows:")
    print("0 | 1 | 2")
    print("----------")
    print("3 | 4 | 5")
    print("----------")
    print("6 | 7 | 8")
    print("When prompted, respond with the index where you want to place your piece.")
    while(True):
        playerFirst = input("Would you like to go first? (y/n)")
        if (playerFirst == "y"):
            player = 1
            break
        elif (playerFirst == "n"):
            player = 2
            break
        else: print("Sorry, that wasn't a proper response. Please try again.")

    gameOver = False
    startingBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    game = TicTacToe(startingBoard)
    game.drawBoard()
    #Game Loop
    while (not gameOver):
        if (player == 1):
            askPlayerForMove(game, player)
        else:
            print("AI's Turn: ")
            AIMove(game)
        game.drawBoard()

        #Check for if game ended
        if (game.checkWin(player)):
            gameOver = True
            break
        else:
            if (player == 1): player = 2
            else: player = 1
    return

if __name__ == '__main__':
    game()
