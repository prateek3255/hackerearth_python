#https://www.hackerearth.com/codearena/ring/6f1ba6e/
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    c=0
    for i in range(m,n+1):
        if str(i)[::-1]==str(i):
            c=c+1
    print(c)


