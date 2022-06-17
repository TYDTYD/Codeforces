import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    plag=False
    if n%2==0:
        sum=0
        idx1=(n//2)-1
        idx2=(n//2)
        while(idx1!=-1):
            sum=sum+a[idx1]+a[idx2]
            if sum==s:
                print(idx1)
                plag=True
                break
            idx1-=1
            idx2+=1
        if plag==False:
            print(-1)
    else:
        idx1=n//2
        idx2=n//2
        sum=a[idx1]
        if a[idx1]==s:
            print(idx1)
            plag=True
        else:
            while(idx1!=-1):
                idx1-=1
                idx2+=1
                sum=sum+a[idx1]+a[idx2]
                if sum==s:
                    print(idx1)
                    plag=True
                    break
            if plag==False:
                print(-1)