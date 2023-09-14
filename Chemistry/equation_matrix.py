import sympy as sp
import re, eq_summary

diatomics = ["h", "n", "o", "f", "cl", "br", "i"]

def solve(reactants, products):
    symbolList = []
    cols = []
    
    for i in range(len(reactants)):
        if reactants[i].lower() in diatomics:
            reactants[i] = reactants[i] + "2"

    for i in range(len(products)):
        if products[i].lower() in diatomics:
            products[i] = products[i] + "2"

    compounds = reactants + products

    for compound in compounds: 
        chunks = re.findall('[A-Z][^A-Z]*', compound)
        for chunk in chunks:
            symbol = ""
            for char in chunk:
                if not char.isdigit():
                    symbol += char
            if symbol not in symbolList:
                symbolList.append(symbol)
    
    for compound in compounds:
        tmp = []
        for symbol in symbolList:
            if symbol in compound:
                elems = re.findall('[A-Z][^A-Z]*', compound)
                for elem in elems:
                    if symbol in elem:
                        num = ""
                        for char in elem[::-1]:
                            if char.isdigit():
                                num += char
                            else:
                                break
                        if num != "":
                            tmp.append(int(num[::-1]))
                        else:
                            tmp.append(1)
            else:
                tmp.append(0)
        cols.append(tmp)
    equationMatrix = sp.Matrix(cols).T.rref()[0].T

    if sp.eye(len(cols)) == equationMatrix:
        print("Error: Elements entered incorrectly.")
        return ["1"]*len(compounds),compounds,"No Summary"
    multiplier = 1
    b = []
    for item in equationMatrix.row(-1):
        b.append(item)
        if item / 1 != item // 1:
            multiplier = sp.lcm(sp.fraction(item)[1], multiplier)
    equationMatrix *= multiplier
    b = [x*multiplier for x in b]
    while 0 in b:
        b.remove(0)
    while len(b) < len(compounds):
        b.append(multiplier)
    b[len(reactants):-1] = [x*-1 for x in b[len(reactants):-1]]
    coefs = [str(x) for x in b]
    return coefs, compounds, eq_summary.summary(coefs, reactants, products)

def main():
    eq = input()
    r,p = eq.split("=")
    r = r.split("+")
    p = p.split("+")
    r = [x.strip() for x in r]
    p = [x.strip() for x in p]
    coefs, compounds, summary = solve(r, p)
    finalString = ""
    for i in range(len(r)):
        finalString += f"{coefs[i]} ( {compounds[i]} ) + "
    finalString = finalString[:-2] + "==> "
    for i in range(len(r), len(r) + len(p)):
        finalString += f"{coefs[i]} ( {compounds[i]} ) + "
    print(finalString[:-2])

if __name__ == "__main__":
    main()