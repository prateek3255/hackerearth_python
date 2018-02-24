t=int(input())
for _ in range(t):
    x,y,n=map(int,input().split())
    l=[y]*x
    while(len(l)<=n):
        s=0
        for i in range(len(l)-1,len(l)-x-1,-1):
            s+=l[i]
        l.append(s)
    print(l[n-1])