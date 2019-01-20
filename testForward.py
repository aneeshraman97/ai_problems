global N

N = 8
global board
global placed

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]
         ]

placed = [0,0,0,0,4,0,0,0]
assigned = [False,False,False,False,True,False,False,False]

def print_board(board):
    string = ""
    for i in range(N):
        for j in range(N):
            string+= str(board[i][j])+"\t"
        string+="\n"

    return string


def pick_queen_to_place():

    for i in range(len(assigned)):
        if(assigned[i]==False):
            return i
    
    return -1

def find_in_list(list_of_objects, to_find):
    for i in range(len(list_of_objects)):
        if(list_of_objects[i]==to_find):
            return i
    
    return -1



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

def solve():
    x = pick_queen_to_place()
    if(x==-1):
        return True
    assigned[x] = True
    current_domain = find_domain(x)
    for d in current_domain:
        placed[x]=d

        if(verify_safety(board,x,d)):
            board[x][d]=1
            if(solve()):
                return True

            board[x][d]=0
    assigned[x]=False
    return False

def find_domain(row):
    final_domain = []
    for i in range(N):
        if((verify_safety(board,row,i))):
            if(len(final_domain)==0):
                final_domain.append(i)
            if(find_in_list(final_domain,(i))==-1):
                final_domain.append(i)

    return final_domain


def main():

    if(solve()==False):
        print("Solution does not exist!!!")
        return False
    
    print("Board after solving : \n"+print_board(board))
    print("Placed Queens : "+str(placed))
    return True


if __name__ == "__main__":
    main()
