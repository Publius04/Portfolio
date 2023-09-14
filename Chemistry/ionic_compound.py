import get_charge
import sympy as sp

def balance_ion(r1, r2):
    if len(r1) >= 2:
        if not r1[1].isdigit():
            r1 = r1[0:2]
    if len(r2) >= 2:
        if not r2[1].isdigit():
            r2 = r2[0:2]
            
    r1charge = get_charge.get_charge(r1)
    r2charge = get_charge.get_charge(r2)
    chargeMatrix = sp.Matrix([[r1charge, r2charge]]).rref()
    if type(chargeMatrix[0][1]) == sp.core.numbers.Rational:
        denom = sp.fraction(chargeMatrix[0][1])[1]
    else:
        denom = 1
    
    r1coef = str(int(-1 * denom * chargeMatrix[0][1]))
    r2coef = str(int(denom * chargeMatrix[0][0]))

    if r1coef == "1":
        r1coef = ""
    if r2coef == "1":
        r2coef = ""

    p = r1 + r1coef + r2 + r2coef
    return p

def main():
    r1 = input("Enter the first element: ")
    r2 = input("Enter the second element: ")
    print(balance_ion(r1, r2))

if __name__ == "__main__":
    main()