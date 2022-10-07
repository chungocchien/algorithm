# tim a^b mod m
import math


def find_mode(a, b, m):
    n = bin(b).replace('0b', '')[::-1]
    x = 1
    power = a % m
    for i in n:
        if i == '1':
            x1 = x * power
            x = x1 % m
        p = power * power
        power = p % m
    return x


def isPrime(n):
    count = 0
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            break
    if count == 0:
        return True
    return False


def find(n):
    m = 0
    a = []
    count = 0
    for i in range(1, int(n/2)):
        if (n - 1) % i == 0 and isPrime(i):
            a.append(i)
    for i in range(2, n):
        for j in a:
            if find_mode(i, int((n - 1) / j), n) == 1:
                count = 0
                break
            if find_mode(i, int((n - 1) / j), n) != 1:
                count += 1
        if count == len(a):
            m = i
            break
    return m

'''f = open('D:\\python\\pythonProject_23_09\\prime.txt', 'r')

character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
value = []
for i in range(0, 26):
    value.append(i)
p = int(f.readline())
a = int(f.readline())
k = int(f.readline())
alpha = find(p)
beta = find_mode(alpha, a, p)
x = 0
ban_ma = open('D:\\python\\pythonProject_23_09\\index.txt', 'r').readline()[::-1]
for i in range(0, len(ban_ma)):
    for j in range(0, 25):
        if character[j] == ban_ma[i]:
            x += value[j] * pow(26, i)
x = x % p
y1 = find_mode(alpha, k, p)
y2 = (find_mode(beta, k, p) * x) % p
print('(y1:', y1, ',y2:', y2, ')')
giaima = (y2 * find_mode(y1, p - a - 1, p)) % p
print(giaima)'''

a = int(input())
b = int(input())
m = int(input())
print(find_mode(a, b, m))
