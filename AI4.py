def solve_n_queens(n):
    board=[-1]*n
    columns=[False]*n
    d1=[False]*(2*n-1)
    d2=[False]*(2*n-1)
    solutions=[]

    def place_queen(row):
        if row==n:
            solutions.append(board.copy())
            return 
        for col in range(n):
            if not columns[col] and not d1[row+col] and not d2[row-col+n-1]:
                board[row]=col
                columns[col]=d1[row+col]=d2[row-col+n-1]=True
                place_queen(row+1)
                columns[col]=d1[row+col]=d2[row-col+n-1]=False

    place_queen(0)
    return solutions

n=4
results=solve_n_queens(n)
x=len(results)
print("Total solutions for ",n ,"queens is:",x,"\n")
for solution in results:
    for row in range(n):
        line=["."]*n
        line[solution[row]]="Q"
        print(" ".join(line))
    print()



