import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    s=input().strip()
    count0=0
    count1=0
    suspect=0
    index1=0
    index2=0
    if len(s)==1:
        print(1)
    elif s[0]=='0':
        print(1)
    elif s[-1]=='1':
        print(1)
    else:
        for j in range(len(s)-1):
            if count0==0 and s[j]=='0':
                index2=j
                count0+=1
                break
            elif s[j]=='1':
                count1+=1
                index1=j
            else:
                index2=j
        if count1==0 and count0==0:
            print(len(s))
        else:
            print(index2-index1+1)