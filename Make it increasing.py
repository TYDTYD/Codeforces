import sys
input=sys.stdin.readline

t=int(input())
plag=True
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    front=len(a)-2
    rear=len(a)-1
    count=0
    while(rear!=0):
        if a[rear]<rear:
            print(-1)
            plag=False
            break
        elif a[front]<a[rear]:
            front-=1
            rear-=1
        else:
            count+=1
            a[front]=a[front]//2
    if plag==True:
        print(count)
    else:
        plag=True