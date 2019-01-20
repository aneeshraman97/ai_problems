global N

N = 8


def print_board(board):
    string = ""
    for i in range(N):
        for j in range(N):
            string+= str(board[i][j])+"\t"
        string+="\n"

    print(string)


def validate_attack(board, row, col):

    for j in range(N):
        if(board[row][j] == 1 or board[j][col] == 1):
            return True

    for i in range(N):
        for j in range(N):
            if((i+j == row+col) or (i-j == row-col)):
                if(board[i][j] == 1):
                    return True

    
    return False

def get_queens_on_board(board):
    queens = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                queens.append((i,j))

    return queens

def verify_safety(board, row, column):
    
    queens = get_queens_on_board(board)
    for queen in queens:
        r, c = queen
        if row == r or column == c:
            return False
        if(abs(row-r)==abs(column-c)):
            return False
    return True


def solve(board, no_of_queens):

    if(no_of_queens == 0):
        return True

    for i in range(N):
        for j in range(N):
            if(verify_safety(board,i,j) and board[i][j]!=-1):
                board[i][j] = 1

                if(solve(board, (no_of_queens-1)) == True):
                    return True

                board[i][j] = 0

    return False


def main():

    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]
             ]

    if(solve(board,7)==False):
        print("Solution Does not Exist!!!")
        return False

    print_board(board)
    return True

if __name__ == "__main__":
    main()
