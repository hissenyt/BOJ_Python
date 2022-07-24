import sys
input=sys.stdin.readline

def cross(a,b,c,w):
    d=(b[0]-a[0],b[1]-a[1])
    e=(c[0]-b[0],c[1]-b[1])
    f=(w[0]-b[0],w[1]-b[1])
    
    x=d[0]*e[1]-d[1]-e[0]
    y=d[0]*f[1]-d[1]-f[0]
    if x*y>0:
        return 
    tmp=a[0]
