#https://www.hackerearth.com/challenge/competitive/may-easy-18/algorithm/sweets-all-around-41706d5f/

n=int(input())
sweets=[]
for _ in range(n):
    l=list(map(int,input().split()))
    sweets.append(l)
a,b=zip(*sweets)
m=max(max(a),max(b))

ma=0;
temp=0;
s=0
for i in range(m):
    temp=0
    for j in sweets:
        if i>=j[0] and i<=j[1]:
            temp+=1
    if temp>ma:
        ma=temp;
        s=i
    elif temp<ma:
        break
print(s,ma,sep=' ')
