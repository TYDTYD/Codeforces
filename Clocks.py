import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    s=list(input().strip())
    s1=s[:]
    index=len(s)
    count=0
    x=''
    for i in range(5,len(s)):
        x+=s[i]
    x=int(x)
    if x>=60:
        hour=x//60
        minute=x-hour*60
    else:
        hour=0
        minute=x
    while(True):
        idx2=str((int(s1[3]+s1[4])+minute)%60)
        plus=(int(s1[3]+s1[4])+minute)//60
        idx1=str((int(s1[0]+s1[1])+hour+plus)%24)
        if len(idx1)==1:
            s1[0]='0'
            s1[1]=idx1
        else:
            s1[0]=idx1[0]
            s1[1]=idx1[1]
        if len(idx2)==1:
            s1[3]='0'
            s1[4]=idx2
        else:
            s1[3]=idx2[0]
            s1[4]=idx2[1]
        if s1[0]==s1[4] and s1[1]==s1[3]:
            count+=1
        if s1==s:
            break

    print(count)