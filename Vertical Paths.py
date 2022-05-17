import sys
input=sys.stdin.readline

def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

t=int(input())

for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    graph=[[] for _ in range(n+1)]
    root=0
    count=0

    for j in range(n):
        if p[j]==j+1:
            root=j
        else:
            graph[p[j]].append(j+1)
    visited=[False]*n
    while visited.count(True)==n:
        dfs(graph,root,visited)
        count+=1
    print(count)