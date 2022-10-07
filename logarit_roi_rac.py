import math



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
    return y2


def discreteLog(prime, base, arg):
    result = 0
    N = prime - 1
    n = 1 + int(math.sqrt(N))
    firstList = {1: 0}
    current = 1
    for i in range(1, n + 1):
        current = current * base % prime
        if not current in firstList:
            firstList[current] = i
    if arg in firstList:
        return firstList[arg]
    else:
        mul = ext_gcd(prime, pow(base, n, prime))
        for i in range(1, n + 1):
            arg = (arg * mul) % prime
            if arg in firstList:
                return (firstList[arg] + n * i)
    return (-1)

base = int(input())
prime = int(input())
arg = int(input())
print(discreteLog(prime, base, arg))


