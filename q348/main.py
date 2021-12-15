# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.board = [[''] * n for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        # make move
        if player == 1:
            self.board[row][col] = 'X'
        elif player == 2:
            self.board[row][col] = 'O'
        # check rows
        if list(set(self.board[row])) == ['O'] or list(set(self.board[row])) == ['X']:
            return player
        # check cols
        cur_col = [j[col] for j in self.board]
        if list(set(cur_col)) == ['O'] or list(set(cur_col)) == ['X']:
            return player
        # check diagonal
        if row == col:
            pos = [self.board[i][i] for i in range(self.n)]
            if list(set(pos)) == ['O'] or list(set(pos)) == ['X']:
                return player
        if row + col == self.n - 1:
            neg = [self.board[i][self.n - 1 - i] for i in range(self.n)]
            if list(set(neg)) == ['O'] or list(set(neg)) == ['X']:
                return player
        return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
    vals=[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
