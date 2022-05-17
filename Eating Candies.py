import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    n=int(input())
    number=2
    answer=0
    candy=list(map(int,input().split()))
    left=0
    leftSum=candy[left]
    right=n-1
    rightSum=candy[right]
    while(left<right):
        if leftSum==rightSum:
            answer=number
            right-=1
            left+=1
            rightSum+=candy[right]
            leftSum+=candy[left]
            number+=2
        elif leftSum>rightSum:
            right-=1
            rightSum+=candy[right]
            number+=1
        elif rightSum>leftSum:
            left+=1
            leftSum+=candy[left]
            number+=1
    print(answer)