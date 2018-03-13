def program(li,thresh):
    greater=[]
    for i in li:
        if len(i)>thresh:
            greater.append(len(i))
    return greater

l=list(input().split())
t=int(input())
print(program(l,t))
    