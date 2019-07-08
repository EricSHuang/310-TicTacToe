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
        """Used at game runtime for checking which player won."""
        board = self.boardState
        victoryMsg = "Player %d Won!" %(board[0])
        #Horizontal Win
        for i in range(3):
            if (board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != 0):
                print(victoryMsg)
        #Vertical Win
        for i in range(3):
            if (board[i] == board[i+3] == board[i+6] and board[i] != 0):
                print(victoryMsg)
        #Diagonal Win
        if (board[0] == board[4] == board[8] and board[0] != 0):
            print(victoryMsg)
        elif (board[2] == board[4] == board[6] and board[2] != 0):
            print(victoryMsg)

    def checkCompWin(self):
        """Used by AI to determine the game outcome when deciding moves."""


if __name__ == '__main__':
    startingBoard = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    start = TicTacToe(startingBoard)
    start.drawBoard()
    start.checkWin()
