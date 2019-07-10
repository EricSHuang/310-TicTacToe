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
        if (self.boardState[place] != 0):
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
    movesArr = []       #TODO: figure out if alg is do-able without this variable
    for i in range(len(game.boardState)):
        if (game.boardState[i] == 0):
            legalMoves[i] = 0
            movesArr.append(i)


    copyGame = copy.deepcopy(game)
    #Heuristic Values
    numPlayouts = 2500
    AIToken = 2
    win = 5
    tie = 4
    lose = -5
    #Do random playouts for each of the legal moves to determine the optimal move
    for move in legalMoves:
        moveGame = copy.deepcopy(copyGame)
        #print("-----------MOVE: %d---------" %(move))
        moveGame.move(AIToken, move)     #TODO: check this line for correctness later
        tempMoves1 = copy.deepcopy(movesArr)   #TODO: think of better name for this var
        tempMoves1.remove(move)

        for i in range(0, numPlayouts):
            randomGame = copy.deepcopy(moveGame)
            """
            print(moveGame.boardState)
            print("random: ")
            randomGame.drawBoard()
            print("move:")
            moveGame.drawBoard()
            print("copy: ")
            copyGame.drawBoard()
            print("original: ")
            game.drawBoard()
            """
            tempMoves = copy.deepcopy(tempMoves1)
            testGameOver = False
            turn = 1
            while (testGameOver == False):
                if (turn % 2 == 1):
                    #random human choice
                    randomHuman = random.choice(tempMoves)
                    randomGame.move(1, randomHuman)
                    tempMoves.remove(randomHuman)
                else:
                    #random AI choice
                    randomAI = random.choice(tempMoves)
                    randomGame.move(2, randomAI)
                    tempMoves.remove(randomAI)

                #check if game is over
                gameState = randomGame.checkCompWin()
                #print("gameState: %d" %(gameState))
                #randomGame.drawBoard()
                #print(tempMoves)
                if (gameState == 0):
                    turn += 1
                else:
                    #TODO: check this too
                    if (gameState == 1): legalMoves[move] += win
                    elif (gameState == 2): legalMoves[move] += lose
                    else: legalMoves[move] += tie
                    #print("got here \n")
                    testGameOver = True
                    break

    print(legalMoves)
    #Choose the optimal move
    #TODO: THIS IS JUST PSEUDO CODE FOR NOW
    """
    bestMove = 0
    bestValue = -2000
    for move in legalMoves:
        print(move)
        print(legalMoves[move])
        if (legalMoves[move] > bestValue):
            bestMove = move
            bestValue = legalMoves
    """
    bestMove = max(legalMoves.items(), key=operator.itemgetter(1))[0]
    #print("bestMove: ", bestMove)
    game.move(AIToken, bestMove)
    return
    #return bestMove

def askPlayerForMove(game, player):
    while (True):
        place = input("Player %d's Turn: " %(player))
        if (game.move(player, int(place)) == True):
            return
        else:
            print("Sorry, that was an illegal move. Please try again.")

def game():
    gameOver = False
    player = 1
    startingBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    game = TicTacToe(startingBoard)
    game.drawBoard()
    while (not gameOver):
        #Check for if game ended
        if (game.checkWin(player)):
            print("check")
            gameOver = True
            break

        if (player == 1):
            askPlayerForMove(game, player)
            player = 2
        else:
            print("AI's Turn: ")
            AIMove(game)
            player = 1
        game.drawBoard()


if __name__ == '__main__':
    game()
