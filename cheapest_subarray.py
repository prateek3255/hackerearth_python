#https://www.hackerearth.com/challenge/competitive/june-easy-18/algorithm/cheapest-subarray-d628cb65/
t=int(input())

for _ in range(t):
    n=int(input())
    m=2*10**4
    l=list(map(int,input().split()))
    for i in range(n):
        k=i+1
        while k<n:
            sub=l[i:k+1]
            temp=min(sub)+max(sub)
            if m>temp:
                m=temp
            k=k+1
    print(m)


