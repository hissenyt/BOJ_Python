import itertools
while True:
    l=list(map(int,input().split()))
    if l==[0]:
        break
    else:
        a=l[0]
        l.remove(l[0])
        l.sort()
        c=itertools.combinations(l,6)
        for i in c:
            for j in i:
                print(j,end=" ")
            print("")
    print("")
