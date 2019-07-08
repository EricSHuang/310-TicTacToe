"""
CMPT310: a4.py
Eric Huang
"""

class TicTacToe:
    def __init__(self, boardState):
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

    def checkWin(self):
        """Used at game runtime for checking which player won.
        Returns True if a player has won, False otherwise."""
        board = self.boardState
        victoryMsg = "Player %d Won!" %(board[0])
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
        elif (board[2] == board[4] == board[6] and board[2] != 0):
            print(victoryMsg)
            return True
        else: return False
        #Ties
        if (board.count(0) == 0):
            return True

    def checkCompWin(self):
        """Used by AI to determine the game outcome when deciding moves.
        Returns 0 on AI wins, 1 on AI losses and 2 on tie games."""
        board = self.boardState
        AI = 2  #Computer's Player Token
        #Horizontal
        for i in range(3):
            if (board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != 0):
                if (board[i*3] == AI):
                    return 0
                else: return 1
        #Vertical
        for i in range(3):
            if (board[i] == board[i+3] == board[i+6] and board[i] != 0):
                if(board[i] == AI):
                    return 0
                else: return 1
        #Diagonal
        if (board[0] == board[4] == board[8] and board[0] != 0):
            if (board[0] == AI):
                return 0
            else: return 1
        elif (board[2] == board[4] == board[6] and board[2] != 0):
            if (board[2] == AI):
                return 0
            else: return 1
        #Ties
        if (board.count(0) == 0):
            return 2

def askPlayerForMove(game, player):
    while (True):
        place = input("Player %d's Turn: " %(player))
        if (game.move(player, int(place)) == True):
            return
        else:
            print("Sorry that was an illegal move. Please try again.")

def game():
    gameOver = False
    player = 1
    startingBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    game = TicTacToe(startingBoard)
    game.drawBoard()
    while (gameOver == False):
        askPlayerForMove(game, player)

        if (game.checkWin() == True):
        #Check for if game ended
            gameOver = True
        else:
            #Swap Player's Turns
            if (player == 1): player = 2
            else: player = 1
            game.drawBoard()

if __name__ == '__main__':
    game()