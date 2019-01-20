global N

N = 8
global board
global placed
global value

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]
         ]

placed = [-1,-1,-1,-1,4,-1,-1,-1]
value = [-1,-1,-1,-1,4,-1,-1,-1]
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


def solve():

    x = pick_queen_to_place()
    if(x==-1):
        return True
    assigned[x] = True
    current_domain = find_domain(x)

    for v in current_domain:
        value[x]=v
        
    for d in current_domain:
        placed[x]=d
        if(not(validate_attack(board,x,d))):
        
            board[x][d]=1
            if(solve()):
                return True

            board[x][d]=0
    assigned[x]=False
    return False
        
    


def find_domain(row):
    final_domain = []
    for i in range(N):
        if(not(validate_attack(board,row,i))):
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
