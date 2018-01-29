#https://www.hackerearth.com/challenge/competitive/january-circuits-18/algorithm/buying-items-d552af6f/
from builtins import int
from operator import itemgetter

m,n=map(int,input().split())
sellers=[]
for _ in range(m):
    *l,c=map(int,input().split())
    l=list(l)
    seller={}
    seller['items']=l
    seller['cost']=c
    seller['total']=n-sum(l)+c
    sellers.append(seller)

sellers = sorted(sellers, key=itemgetter('total')) 
# print(sellers)

buyer=[0 for _ in range(n)]
total_cost=0

for seller in sellers:
    buyer=list(map(sum, zip(*[buyer,seller['items']])))
    total_cost+=seller['cost']
#     print(buyer,total_cost)
    if sum(buyer)>=n:
        break
print(total_cost)


