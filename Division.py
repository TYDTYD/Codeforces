import sys
input=sys.stdin.readline

n=int(input())
rating=[]

for i in range(n):
    rating.append(int(input()))

for i in rating:
    if i<=1399:
        print("Division 4")
    elif i<=1599 and i>=1400:
        print("Division 3")
    elif i<=1899 and i>=1600:
        print("Division 2")
    else:
        print("Division 1")