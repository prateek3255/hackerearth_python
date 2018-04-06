#https://www.hackerearth.com/codearena/ring/4e371eb/
s=input()
all_char=set(map(str,s))
m=0
ch=' '
for i in all_char:
    a=s.count(i)
    if a>=m:
        if a==m:
            if ord(i)>ord(ch):
                ch=i
                m=a
        else:
            ch=i
            m=a
            
print(ch,m)


