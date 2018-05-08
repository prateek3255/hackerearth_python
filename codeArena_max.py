#https://www.hackerearth.com/codearena/ring/1789e72/
def factors(n):
    facts=set()
    for i in range(1,n+1):
        if n%i==0:
            facts.add(i)
    return facts

m=int(input())
_=input()
fm=factors(m)
l=list(map(int,input().split()))
count=0
for i in l:
    fl=factors(i)
    if len(fl.intersection(fm))>1:
        count+=1
print(count)


