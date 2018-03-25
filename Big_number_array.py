#https://www.hackerearth.com/challenge/competitive/march-circuits-18/algorithm/big-number-array-043361b7/

def flip(b,j):
    if b[j]=='0':
        b=b[:j]+'1'+b[j+1:]
    else:
        b=b[:j]+'0'+b[j+1:]
    return b
    
t= int(input())    
for _ in range(t):
    n,q=map(int,input().split())
    a=[0]*n
    for _ in range(q):
        ty,*l=map(int,input().split())
        if ty==1:
            x=l[0]
            y=l[1]
            I=l[2]
            r=l[3]
            for i in range(x-1,y):
                b="{0:b}".format(a[i])
                if len(b)<r:
                    b=b+'0'*(r-len(b)+1)
                for j in range(I,r+1):
                    b=flip(b,j)
                a[i]=int(b,2)
        else:
            x=l[0]
            y=l[1]
            if a[x-1]==a[y-1]:
                print("YES")
            else:
                print("NO")            
        
