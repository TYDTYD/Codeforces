t=int(input())

for i in range(t):
    n=int(input())
    possible=True
    Rindex=0
    Bindex=0
    stamp=list(input())
    for j in range(n):
        if stamp[j]=='B':
            Bindex+=1
        elif stamp[j]=='R':
            Rindex+=1
        if stamp[j]=='W' or j==n-1:
            if Bindex==0 and Rindex!=0:
                print("NO")
                possible=False
                break
            elif Rindex==0 and Bindex!=0:
                print("NO")
                possible=False
                break
            Bindex=0
            Rindex=0
    if possible==True:
        print("YES")