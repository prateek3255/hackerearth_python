# https://www.hackerearth.com/codearena/ring/ba3558c/


n=int(input());
for i in range(n):
    k,n=map(int,input().split());
    nodes=k**(n+1)-1;
    modulo=0
    while nodes!=0:
        modulo+=int(nodes%10);
        nodes=int(nodes/10);
        
    print(modulo)

