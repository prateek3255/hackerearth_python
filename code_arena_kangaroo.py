#https://www.hackerearth.com/codearena/ring/a36165d/
t=int(input())
for _ in range(t):
    a,b,m=map(int,input().split())
    start=a+(m-a%m)
    end=b-(m-a%m)
    count=(end-start)/m+1
    print(int(count))