def check(c,d):
    for i in range(3):
        if c==d:
            return True
        else:
            tm=c[0]
            c.remove(c[0])
            tp=d[0]
            d.remove(d[0])
            c.append(tm)
            d.append(tp)
    return False
import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    a,b=l[0:4],l[4:8]
    if a==b:
        print(1)
    else:
        bot=a[0]
        if b[0]==bot:
            c=a[1:]
            d=b[1:]
        same=False
        for j in range(3):
            if check(c,d):
                print(1)
                
        if same=True:
            print(1)
        else:
