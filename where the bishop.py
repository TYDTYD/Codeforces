import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    chessboard=[[] for _ in range(8)]
    input()
    for j in range(8):
        chessboard[j]=list(input().strip())

    for m in range(1,7):
        for n in range(1,7):
            if chessboard[m][n]=='#' and chessboard[m-1][n-1]=='#' and chessboard[m-1][n+1]=='#' and chessboard[m+1][n-1]=='#' and chessboard[m+1][n+1]=='#':
                print(m+1,n+1)
                break