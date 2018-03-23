#https://www.hackerearth.com/challenge/competitive/march-circuits-18/algorithm/big-number-array-043361b7/
t= int(input())

for _ in range(t):
    n,q=map(int,input().split())
    a=[0]*n
    ty,*l=map(int,input().split())
    if ty==1:
        x=l[0]
        y=l[1]
        I=l[2]
        r=l[3]
        
