global N

N = 8
global threat_list
global board

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]
         ]

threat_list=[[1, 0, 0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 1, 0, 0, 1]
         ]

placed = [0,0,0,0,4,0,0,0]

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

def find_initial_threats():
    for i in range(N):
        row_list=[]
        for j in range(N):
            if(validate_attack(board,i,j)):
                row_list.append(1)
            else:
                row_list.append(0)
        threat_list.append(row_list)
    return threat_list

def print_board(board):
    string = ""
    for i in range(N):
        for j in range(N):
            string += str(board[i][j])+"\t"
        string += "\n"

    print(string)


def solve(board, col):

    if(col == N):
        return True

    for i in range(N):
        if(threat_list[i][col] == 0):
            placed[col] = i
            add_threats(i, col)
            if(validate(col)):
                solve(board, col+1)

            remove_threats(i, col)

    return False


def determine_threats(modifier, row, col):
    for j in range(1,N-col):
        if(threat_list[row][col+j]!=1):
            threat_list[row][col+j] += modifier  # horizontal threats
        if(row+j < N):
            if(threat_list[row+j][col+j]!=1):
                threat_list[row+j][col+j] += modifier  # diagonal threats
        if(row-j >= 0):
            if(threat_list[row-j][col+j]!=1):
                threat_list[row-j][col+j] += modifier  # diagonal threats


def add_threats(row, col):
    determine_threats(1, row, col)


def remove_threats(row, col):
    determine_threats(-1, row, col)


def validate(col):

    for i in range(col+1, N):
        can_place = False
        for row in range(N):
            if(can_place):
                break
            if(threat_list[row][i] == 0):
                can_place = True

        if(can_place == False):
            return False

    return True


def main():

    #print("Init",find_initial_threats())
    if(solve(board, 0) == False):
        print("Solution Does not Exist!!!")
        return False

    print_board(board)
    return True


if __name__ == "__main__":
    main()
