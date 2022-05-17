import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    a,b,c,x,y=map(int,input().split())
    if x>=a:
        x=x-a
    else:
        x=0
    if y>=b:
        y=y-b
    else:
        y=0
    sum=x+y
    if sum>c:
        print("NO")
    else:
        print("YES")