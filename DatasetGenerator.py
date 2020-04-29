import numpy as np
import csv
import math
import random
from sympy import *  


with open('2.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    for r in range(10000):
        max_degree = 5
        x = symbols('x')
        num_size = np.random.randint(1, max_degree)
        num_coefs = [0] * num_size
        num_coefs_ds = [0] * max_degree
        for ind in range(num_size):
            rand_coef = random.randint(-100, 100)
            #if(ind != num_size - 1 or (ind == num_size - 1 and rand_coef != 0)):
            num_coefs[ind] = rand_coef
            num_coefs_ds[ind] = rand_coef
        denom_size = np.random.randint(1, max_degree)
        denom_coefs = [0] * denom_size
        denom_coefs_ds = [0] * max_degree
        for ind in range(denom_size):
            rand_coef = random.randint(-100, 100)
            #if(ind != denom_size - 1 or ((ind == denom_size - 1) and rand_coef != 0)):
            denom_coefs[ind] = rand_coef
            denom_coefs_ds[ind] = rand_coef
        while(len(denom_coefs) != 0 and denom_coefs[len(denom_coefs) - 1] == 0):
            del denom_coefs[-1]
        while(len(num_coefs) != 0 and num_coefs[len(num_coefs) - 1] == 0):
            del num_coefs[-1]
        denom_size= len(denom_coefs)
        num_size = len(num_coefs)
        #expr = (np.polyval(num_coefs, x)  / np.polyval(denom_coefs, x))
        if(len(denom_coefs) != 0 and len(num_coefs) != 0):
            for d in range(len(denom_coefs)):
                if(denom_coefs[d] != 0):
                    is_zero = False
            if(is_zero == False):
                c = 0
                value_at = random.randint(-100, 100)
                while(c != len(num_coefs)):
                    for last_coeff in range(100):
                        #value_at = random.randint(-100, 100)
                        lim = round(my_limit(num_coefs, denom_coefs, value_at), 3)
                        if(lim == -0):
                            lim = 0
                        if np.isnan(lim) == False and math.isinf(lim) == False and lim > -1000 and lim < 1000:
                            allcontent=np.concatenate((num_coefs_ds,denom_coefs_ds,[value_at,lim]), axis = None)
                            writer.writerow(allcontent)
                        print("Num Size", c)
                        num_coefs[num_size - 1 - c] = random.randint(-100, 100)
                        num_coefs_ds[num_size - 1 - c] = num_coefs[num_size - 1 - c]
                    c = c + 1
                d = 0
                while(d != len(denom_coefs)):
                    for f in range(100):
                        #value_at = random.randint(-100, 100)
                        lim = round(my_limit(num_coefs, denom_coefs, value_at), 3)
                        if(lim == -0):
                            lim = 0
                        if np.isnan(lim) == False and math.isinf(lim) == False and lim > -1000 and lim < 1000:
                            allcontent=np.concatenate((num_coefs_ds,denom_coefs_ds,[value_at,lim]), axis = None)
                            writer.writerow(allcontent)
                        print("denom Size", denom_size)
                        print("d", d)
                        denom_coefs[denom_size - 1 - d] = random.randint(-100, 100)
                        denom_coefs_ds[denom_size - 1 - d] = denom_coefs[denom_size - 1 - d]
                    d = d + 1
                for p in range(100):
                    value_at = random.randint(-100, 100)
                    lim = round(my_limit(num_coefs, denom_coefs, value_at), 3)
                    if(lim == -0):
                        lim = 0
                    if np.isnan(lim) == False and math.isinf(lim) == False and lim > -1000 and lim < 1000:
                        allcontent=np.concatenate((num_coefs_ds,denom_coefs_ds,[value_at,lim]), axis = None)
                        writer.writerow(allcontent)
            
num = np.polyval([6,2,3,8,2,16,5,9,1,2,0.0], x)
den = np.polyval([7,2,8,3,5,1,1,9,2,7,0.0,5,0], x)
g = limit(num / den, x, 5)


