import numpy as np
import sympy
import math
import fractions as f

ls = []

def u(x):
    res = 1 - x + pow(x, 2) - pow(x, 3) + pow(x, 4) - pow(x, 5) + pow(x, 6) - pow(x, 7) + pow(x, 8) - pow(x, 9) + pow(x, 10)
    return res

def op(k, n):
    matrix = []
    #first create matrix
    for rownum in range(k):
        row = []
        for item in range(k):
            row.append(pow(rownum + 1, item))
        row.reverse()
        row.append(u(rownum + 1))
        matrix.append(row)

    #then row reduce
    matrix = np.matrix(matrix)
    matrix = sympy.Matrix(matrix).rref(pivots = False)

    #row reduction normalizes by default, so normalization needs to be undone
    for x in range(k - 1):
        fact = 1
        for y in range(k + 1):
            if math.floor(matrix[x, y]) != matrix[x, y]:
                tmp = f.Fraction(matrix[x, y])
                fact *= tmp.denominator()
        if fact != 1:
            for y in range(k + 1):
                matrix[x, y] *= fact

    #get polynomial coefficients
    poly = []
    for item in matrix[:, k]:
        poly.append(item)

    #print polynomial    
    '''
    string = ""
    for i in range(len(ans)):
        if ans[i] > 0:
            string += " +"
        string += str(ans[i])
        if len(ans) - i - 1 == 1:
            string += "x"
        elif len(ans) - i - 1 > 0:
            string += f"x^{len(ans) - i - 1} "
        

    print(string[1:])
    '''

    #return nth term 
    poly.reverse()
    ans = 0
    for i in range(len(poly)):
        ans += pow(n, i) * poly[i]

    return ans

def solve():
    ans = 0
    for i in range(10):
        ans += op(i + 1, i + 2)
    return ans

print(solve())