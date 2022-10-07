def ext_gcd(a,b):
    x1=0
    x2=1
    y1=1
    y2=0
    while b!=0:
        q=int(a/b)
        r=a%b
        x=x2-q*x1
        y=y2-q*y1
        a=b
        b=r
        x2=x1
        x1=x
        y2=y1
        y1=y
        print(a,' ',b,' ',q," ",r," ",x," ",y," ",x1,' ',x2,' ',y1,' ',y2,' ')
    return y2


a=int(input())
b=int(input())

print(ext_gcd(a, b))


