# https://www.hackerearth.com/challenge/competitive/january-circuits-18/algorithm/theatre-830bdbff/
from builtins import int

def minimal(t1,a1,b1,c1,k1):
    li=[]
    s=0
    for i in a1:
        s=s+(i+t1)%k1
    li.append(s)
    s=0
    for i in b1:
        s=s+(i+t1)%k1
    li.append(s)
    s=0
    for i in c1:
        s=s+(i+t1)%k1
    li.append(s)
    return max(li)

n,k=map(int,input().split());
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

t=round((sum(a)+sum(b)+sum(c))/(len(a)+len(b)+len(c)))
# print((len(a)+len(b)+len(c)))
t2=t
t3=t   
while(t2>0 and minimal(t2-1,a,b,c,k)<=minimal(t2,a,b,c,k)):
    t2=t2-1
while(minimal(t3+1,a,b,c,k)<=minimal(t3, a, b, c, k)):
    t3=t3+1
print(min([minimal(t2,a,b,c,k),minimal(t3, a, b, c, k)]))
