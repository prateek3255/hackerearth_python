#https://www.hackerearth.com/challenge/competitive/february-circuits-18/algorithm/simple-sum-3-f1585a25/
n=int(input())
l=list(map(int,input().split()))

s=0
for i in range(0,n):
    for j in range(i,n):
        s+=max(l[i:j+1])*(l[i]|l[j])
print(s) 
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    buses={}
    i=1
    for d in l:
        if i not in buses:
            buses[i]=[d]
        elif len(buses[i])<2:
           buses[i].append(d)
        else:
           i=i+1
    print(buses)