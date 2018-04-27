#https://www.hackerearth.com/challenge/competitive/april-circuits-18/algorithm/t1-1-6064aa64/
n=int(input())
l=list(map(int,input().split()))
ol=list(l)
l.sort()
count=0
while(l!=ol):
    i=0
    for i in range(n):
        if ol[i]!=l[i]:
            a=ol.index(l[i])
            break
    x=l[i:a+1]
    x.reverse()
    l[i:a+1]=x
    count+=1
print(count)


