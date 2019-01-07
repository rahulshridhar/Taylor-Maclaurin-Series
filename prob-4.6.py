#script: prob-4.6.py
#author: Rahul Shridhar
#problem 4.6, p.108

import math
import _series

print("problem 4.6")

def f(x): return math.log(x)

def dfdx(i, x):
    return {
        0: f(x),
        1: 1/x,
        2: -1/x**2,
        3: 2/x**3,
        4: -6/x**4
    }.get(i,0)

xi = 1.0
xiplus1 = 2.5
tv = f(xiplus1)
h = xiplus1 - xi

for i in range(5):
    av = _series.taylor(dfdx, i, xi, h)
    et = abs(1-av/tv)
    print("i = {}, av = {}, tv = {}, et = {:%}".format(i,av,tv,et))
