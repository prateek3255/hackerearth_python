#https://www.hackerearth.com/codearena/ring/a26ff2f/

n,k,l,q=map(int,input().split())
dic={}
for _ in range(n):
    name,*t=input().split()
    t=tuple(map(int,t))
    dic[t]=name
for _ in range(q):
    r=tuple(map(int,input().split())) 
    if r in dic:
        print(dic[r])
    else:
        print("You cant fool me :P")   



