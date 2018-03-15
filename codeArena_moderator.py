# https://www.hackerearth.com/codearena/ring/e170c93/
import operator
n=int(input());
c=[]
for i in range(n):
    t=input()
    s=int(str(t[0:2]+t[3:5]))
    e=int(str(t[6:8]+t[9:11]))
    c.append([s,e])
c.sort(key=operator.itemgetter(1,0))
# print(c)
flag=False
for i in range(n):
    if i<n-1 and (c[i+1][0]-c[i][1])<0:
#         print(c[i][1]-c[i+1][0])
        flag=True
        break
    
if flag:
    print("Will need a moderator!")
else:
    print("Who needs a moderator?")

