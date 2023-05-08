N = 9

board = []
for i in range(N):
    raw = input()
    board.append(list(raw))

count = 0
for i in range(N): #upper left
    for j in range(N):
        if(board[i][j] == "#"):
            for k in range(0, i+1):
                for l in range(j+1, N):
                    if board[k][l] == "#": #upper right
                        y = i-k
                        x = l-j
                        if(i+x < N and j+y < N and k+x < N and l+y < N):
                            if(i+x >= 0 and j+y >= 0 and k+x >= 0 and l+y >= 0):
                                if(board[i+x][j+y] == "#" and board[k+x][l+y] == "#"):
                                    count+=1
                                
print(count)