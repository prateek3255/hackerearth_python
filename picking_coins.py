#https://www.hackerearth.com/challenge/competitive/december-circuits-18/algorithm/picking-the-coins-50470dca/
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    turn=True
    i=1
    while True:
        sub=k**i
        if n-sub>=0:
            n=n-sub
        else:
            turn=True
            break
        if n-sub>=0:
            n=n-sub
        else:
            turn=False
            break
        i+=1

    if turn:
        print("Bob")
    else:
        print("Alice")


