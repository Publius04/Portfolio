import re, get_mass
from tabulate import tabulate

def main():
    eq = input("Enter balanced equation: ")
    r,p = eq.split("=")
    r = r.split("+")
    p = p.split("+")
    r = [x.strip() for x in r]
    p = [x.strip() for x in p]
    print("Select element: ")
    for i, x in enumerate(r):
        print(i, ":", x)
    base = r[int(input())]
    # Calculating base reactant coefficient
    base_reactant = ""
    base_coef = ""
    first = True
    for i in range(len(base)):
        if base[i].isdigit() and first:
            base_coef += base[i]
        else:
            first = False
            base_reactant += base[i]
    if base_coef == "":
        base_coef = 1
    else:
        base_coef = int(base_coef)
    units = input("Moles (0) or grams (1): ")
    
    if units == "0":
        base_moles = float(input("Enter number of moles: "))
    elif units == "1":
        grams = float(input("Enter grams: "))
        mass = get_mass.get_mass(base_reactant)
        base_moles = grams / mass

    p_coefs = []
    p_products = []
    for product in p:
        i = 0
        first = True
        for c in product:
            if c.isdigit() and first:
                i += 1
            else:
                first = False
        if i == 0:
            p_coefs.append(1)
        else:
            p_coefs.append(int(product[:i]))
        p_products.append(product[i:])
    
    p_moles = []
    p_grams = []
    for i in range(len(p)):
        ratio = p_coefs[i] / base_coef
        p_moles.append(ratio * base_moles)
        p_gram = get_mass.get_mass(p_products[i])
        p_grams.append(ratio * base_moles * p_gram)
    print("Yield summary: ")
    print(tabulate([["Product"] + p_products, ["Moles"] + p_moles, ["Grams"] + p_grams]))

if __name__ == "__main__":
    main()