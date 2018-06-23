#https://www.hackerearth.com/challenge/competitive/may-circuits-18/algorithm/plus-plus-60bcac48/

def mul(a,b,l):
    s=((l[a[0]][a[1]]*l[b[0]][b[1]])
    +(l[a[0]-1][a[1]]*l[b[0]-1][b[1]])
    +(l[a[0]+1][a[1]]*l[b[0]+1][b[1]])
    +(l[a[0]][a[1]-1]*l[b[0]][b[1]-1])
    +(l[a[0]][a[1]+1]*l[b[0]][b[1]+1]));
    return s;
    
l=[]
n,m=map(int,input().split())

for _ in range(n):
    l.append(list(map(int,input().split())))
plus={}
for i in range(1,n-1):
    for j in range(1,m-1):
        plus[(i,j)]={(i-1,j),(i+1,j),(i,j),(i,j-1),(i,j+1)}
mx=0

for i in plus:
    for j in plus:
        if i!=j and plus[i].intersection(plus[j])==set():
            k=mul(i,j,l)
            if mx<k:
                mx=k
print(mx)