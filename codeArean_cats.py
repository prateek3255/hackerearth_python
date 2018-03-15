#https://www.hackerearth.com/codearena/ring/bc1fbb5/
n=int(input())
s=list(map(int,input().split()))
c=list(map(int,input().split()))
s.sort()
c.sort()
m=sum([a*b for a,b in zip(s,c)])
print(m)