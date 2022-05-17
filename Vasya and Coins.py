import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
    a,b=map(int,input().split())
    if a==0:
        print(1)
    else:
        print((a+2*b)+1)