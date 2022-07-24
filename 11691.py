def eulerphi2(n):
    if n in [1,2]:return 1
    elif n in [3,4]:return 2
    ans=n
    ret=True
    for i in range(2,int(n**.5)+2):
        if n%i==0:
            ret=False
            exp=1
            n//=i
            while n%i==0:
                n//=i
                exp+=1
            return i**(exp-1)*(i-1)*eulerphi2(n)
    if ret:return n-1