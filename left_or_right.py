# https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/left-or-right-92c0b54c/
n, q=map(int,input().split())
l=list(map(int,input().split()))

for _ in range(q):
    y,z,d=input().split()
    y=int(y)
    z=int(z)
    t_c=l[y]
    count=0
    if z in l:
        while t_c!=z:
            if d=='L':
                y=(y-1+n)%n
            else:
                y=(y+1)%n
            t_c=l[y]
            count+=1
        print(count)
    else:
        print(-1)
                 
