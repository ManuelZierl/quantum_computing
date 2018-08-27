import random

import sys

import math


def ggt(a, b):
    if a == 0:
        return b
    else:
        while b != 0:
            if a > b:
                a = a-b
            else:
                b = b-a
        return a
print((7**12)%45)

print(ggt( 12, 24))

def classical_periode_detecor(a,n):
    # detetect the period of a**x % n
    # this might not be efficient or perfect
    x = 1
    while (a**x) % n != 1:
        sys.stdout.write(str((a**(x+1)) % n) + " ")
        x += 1
    sys.stdout.write("\n")
    return x

print(classical_periode_detecor(7, 45))

#SHOR'S Algorithm
def shor(n):
    # 1. random numer from {2, ..., n-1}
    a = random.randint(2,n) # N-1 ?ermitteln

    # 2. ggt (a,n) -> if != 1 return z
    z = ggt(a,n)
    if n != 1: return z

    # 3. qunatum determine period of a**x mod(n)





x = math.e**(2*math.pi*1j*0/5)
print(x)
print(x**5)

