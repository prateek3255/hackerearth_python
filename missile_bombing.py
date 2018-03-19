#https://www.hackerearth.com/challenge/competitive/march-circuits-18/algorithm/missile-bombing-cd56ab51/
import numpy as np
n=int(input())
m=int(input())
arr=np.zeros((n,n),np.int64)
for _ in range(m):
    p,a,b,c,d=map(int,input().split())
    for i in np.arange(a-1,c):
        for j in np.arange(b-1,d):
            arr[i][j]=arr[i][j]^p
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()




