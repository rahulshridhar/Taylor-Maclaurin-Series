#script: prob-4.2.py
#author: Rahul Shridhar
#problem 4.2, p.108

import math
import _series

print("problem 4.2")

x = math.pi/3
print("x = {} ({:.2f} degrees)".format(x, x*180/math.pi))
tv = math.cos(x)
print("tv = f(x) = {}".format(tv))

print('implementing maclaurin series directly...')

def cos_maclaurin(n,x):
    sum = 0
    for i in range(n+1):
        sum += (-1)**i * x**(2*i) / math.factorial(2*i)
    return sum

for i in range(6):
    av = cos_maclaurin(i,x) #approximated value up to ith order
    et = 1 - av/tv
    print('i = {}, tv = {}, av = {}, et = {:%}'.format(i,tv,av,et))

print('using the taylor series... (maclaurin is equiv. to taylor series when xi=0)')

def dfdx(i,x):
    return {
        0: math.cos(x),
        1: -math.sin(x),
        2: - math.cos(x),
        3: math.sin(x)
    }[i % 4]

xi = 0
h = x - xi  #h = x since xi = 0

for i in range(12):
    av = _series.taylor(dfdx, i, xi, h) #approximated value up to ith order
    et = 1 - av/tv
    if (i % 2): print('i = {}, tv = {}, av = {}, et = {:%}'.format(i,tv,av,et))
