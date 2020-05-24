# main
from group import Group
import sympy, math
from sympy import *
import random

def getOrder(m, N):
    odr = 1;
    m0 = m % N
    m = m % N
    while (m != 1):
        odr += 1
        m *= m0
        m = m % N
    return odr

class BigGroup():
    def __init__(self, N):
        self.N = N
        self.elements = [];
        if (sympy.N == True):
            self.elements = range(1, N);
        else:
            for i in range(1, N):
                if (math.gcd(i, N) == 1):
                    self.elements.append(i);
        self.phi = len(self.elements)
        self.orders = [];
        for element in self.elements:
            self.orders.append(getOrder(element, self.N))

def PHI(N):
    return BigGroup(N).phi

def POW(b, e):
    return int(b ** e)

def splite2(x):
    num = 0
    while (x % 2 == 0):
        x /= 2
        num += 1
    return x, num

def getPrimes(end, start=2):
    lis = []
    for i in range(start, end):
        if (isprime(i)):
            lis.append(i)
    return lis

def maxPrimeFactor(n):
   # number must be even
   while n % 2 == 0:
      max_Prime = 2
      n /= 2
   # number must be odd
   for i in range(3, int(math.sqrt(n)) + 1, 2):
      while n % i == 0:
         max_Prime = i
         n = n / i
   # prime number greator than two
   if n > 2:
      max_Prime = n
   return int(max_Prime)


# sampling = random.sample(getPrimes(50), k=3)
# N = sampling[0] * sampling[1] * sampling[2]

# print(sampling)

N = 53 * 157 * 1613
# base, num = splite2(PHI(N))
# print(N, ": ", math.gcd(PHI(N)//5-1, N))

# print(math.gcd(POW(3, 52)-1, N))
# N = 19 * 11 *5
# base, num = splite2(PHI(N))
# for i in range(0, num + 1):
#     print(base, ": ", math.gcd(POW(2, base)-1, N))
#     base *= 2


# for i in BigGroup(N).elements:
#     print(i, ": ", math.gcd(POW(i,PHI(N)/8)-1, N))

# mydict = {}

for i in getPrimes(100000,5):
    print("p=",i, ", O(2)=", getOrder(2, i), ", O(3)=", getOrder(3, i))
    
    

