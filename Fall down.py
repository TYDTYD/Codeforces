import sys
input=sys.stdin.readline

def dfs(x,y):
    if x+1>=n or x+1<=-1 or y>=m or y<=-1:
        return False
    if graph[x+1][y]=='*' or graph[x+1][y]=='o':
        return False
    else:
        graph[x][y]='.'
        graph[x+1][y]='*'
        dfs(x+1,y)
        return True

t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    graph=[]

    for j in range(n):
        graph.append(list(input().strip()))
    
    for k in range(n-2,-1,-1):
        for l in range(m-1,-1,-1):
            if graph[k][l]=='*':
                dfs(k,l)
    
    for a in range(n):
        for b in range(m):
            print(graph[a][b],end='')
        print()