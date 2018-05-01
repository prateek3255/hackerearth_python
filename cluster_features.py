#https://www.hackerearth.com/challenge/competitive/may-easy-18/algorithm/cluster-features-b6d64df9/
p,q=map(int,input().split())
points=[]
for _ in range(p):
    l=list(map(int,input().split()))
    points.append(l)
for _ in range(q):
    x1,x2,y1,y2=map(int,input().split())
    vp=[]
    for point in points:
        if point[0]>=x1 and point[0]<=x2 and point[1]>=y1 and point[1]<=y2:
            vp.append(point)
    x,y=zip(*vp)
    if len(vp)<1:
        r=0
        d=0
    elif len(vp)<2:
        d=0
        x0=sum(x)/len(vp)
        y0=sum(y)/len(vp)
        s=0
        for i in vp:
            s=s+(x0-i[0])**2+(y0-i[1])**2
        r=(s/len(vp))**1/2
    else:
        x0=sum(x)/len(vp)
        y0=sum(y)/len(vp)
        s=0
        for i in vp:
            s=s+(x0-i[0])**2+(y0-i[1])**2
        r=(s/len(vp))**1/2
        s=0
        for i in vp:
            for j in vp:
                s=s+(j[0]-i[0])**2+(j[1]-i[1])**2
        d= (s/len(vp)*(len(vp)-1))**1/2
    
    n=len(vp)
    out=n*x0+n*y0+n**2*r**2+n*(n-1)*d**2
    print(r,d,int(out))
            
        
        




