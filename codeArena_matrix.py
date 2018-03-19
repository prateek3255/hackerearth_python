import numpy as np
n,r,c=map(int,input().split());
arr=[]
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
if r!=0:
    rows=list(map(int,input().split()))
if c!=0:
    columns=list(map(int,input().split()))
a=np.array(arr)
if r!=0:
    for i in rows:
        arr[i-1]=arr[i-1][1:]+arr[i-1][:1]
if c!=0:
    for i in columns:
        arr[:][i-1]=arr[:][i-1][1:]+arr[:][i-1][:1]
        
print(arr)