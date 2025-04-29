def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row, n):
    # If all queens are placed, return True
    if row == n:
        return True

    # Try placing the queen in all columns one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False


def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()


def n_queens(n):
    board = [[0] * n for _ in range(n)]  # Create an empty chessboard
    if solve_n_queens(board, 0, n):
        print_solution(board, n)
    else:
        print("Solution does not exist")


# Example usage:
n = 12 # Change n to the desired size of the chessboard
n_queens(n)
