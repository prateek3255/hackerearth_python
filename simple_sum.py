#https://www.hackerearth.com/challenge/competitive/february-circuits-18/algorithm/simple-sum-3-f1585a25/
n=int(input())
l=list(map(int,input().split()))

s=0
for i in range(0,n):
    for j in range(i,n):
        s+=max(l[i:j+1])*(l[i]|l[j])
print(s) 
