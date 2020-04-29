from sympy import * 
from fractions import Fraction 
from decimal import Decimal
x = symbols('x')

import numpy as np

from numpy.polynomial.polynomial import polyval
import math
import random

def my_limit(p, q,value_at):
    if(len(p) == 0 or len(q) == 0):
        return np.nan
    if(value_at == oo):
        if(len(p) > len(q)):
            return oo #1,0
        elif(len(p) < len(q)):
            return 0 #0,1
        else:
            return p[len(p) - 1] / q[len(q)-1]  #rotio(val)
    while(polyval(value_at, p) == 0 and polyval(value_at, q) == 0):
        p = derivative(p)
        q = derivative(q)
        if(np.isnan(p) or np.isnan(q)):
            return np.nan
    if(polyval(value_at, q) != 0):
        return polyval(value_at, p) / polyval(value_at, q)
    else:
       return oo 
#return float('NaN')

def derivative(f):
    if(len(f) == 0):
        return np.nan
    df = [0] * (len(f) - 1)
    for coef in range(len(f) - 1):
        df[coef] = f[coef + 1] * (coef + 1)
    return df


