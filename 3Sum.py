import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    n=int(input())
    array=list(map(int,input().split()))
    plag=False
    for a in range(n-2):
        if plag==True:
            break
        for b in range(n-1):
            if plag==True:
                break
            for c in range(n):
                if a>=b or b>=c or a>=c:
                    continue
                if str(array[a]+array[b]+array[c])[-1]=='3' and plag==False:
                    print("YES")
                    plag=True
                    break
    if plag==False:
        print("NO")