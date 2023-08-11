print("Abrar Shaik")
def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True
def solve_queen_problem(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            
            if solve_queen_problem(board, row + 1):
                return True
            board[row][col] = 0
    return False


def eight_queen_problem():
    board = [[0 for _ in range(8)] for _ in range(8)]
    if solve_queen_problem(board, 0):
        for i in range(len(board)):
            for j in range(len(board)):
                print(board[i][j], end=" ")
            print()
    else:
        print("No solution found.")


if __name__ == "__main__":
    eight_queen_problem()
