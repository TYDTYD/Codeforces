import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    n=int(input())
    array=[0]+list(map(int,input().split()))
    plag1=False
    plag2=False
    possible=True
    for j in range(1,n+1):
        if j==1:
            if array[j]%2==0:
                plag1=True
        elif j==2:
            if array[j]%2==0:
                plag2=True
        elif plag1==True and j%2!=0:
            if array[j]%2!=0:
                print("NO")
                possible=False
                break
        elif plag2==True and j%2==0:
            if array[j]%2!=0:
                print("NO")
                possible=False
                break
        elif plag1==False and j%2!=0:
            if array[j]%2==0:
                print("NO")
                possible=False
                break
        elif plag2==False and j%2==0:
            if array[j]%2==0:
                print("NO")
                possible=False
                break
    if possible==True:
        print("YES")

