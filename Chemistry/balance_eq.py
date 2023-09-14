import json, get_charge, ionic_compound, re, equation_matrix, eq_summary

stream = open("ptable.json")
ptable = json.load(stream)
stream.close()

def simple_balance(r1, r2, isIonic, type):
    r1 = r1.title()
    r2 = r2.title()

    if not isIonic:
        p = input("Enter covalent compound: ")
    else:
        p = ionic_compound.balance_ion(r1, r2)

    if type == "s":
        return equation_matrix.solve([r1, r2], [p])
    else:
        return equation_matrix.solve([p], [r1, r2])

def synthesize(r1, r2, isIonic):
    coefs, compounds, summary = simple_balance(r1, r2, isIonic, "s")
    r1, r2, p = compounds
    finalString = f"{coefs[0]} ( {r1} ) + {coefs[1]} ( {r2} ) ==> {coefs[2]} ( {p} )"
    return finalString

def decompose(p1, p2, isIonic):
    coefs, compounds, summary = simple_balance(p1, p2, isIonic, "d")
    r, p1, p2 = compounds
    finalString = f"{coefs[0]} ( {r} ) ==> {coefs[1]} ( {p1} ) + {coefs[2]} ( {p2} ) "
    return finalString

def singleReplace(r1, r2):
    r2elems = re.findall('[A-Z][^A-Z]*', r2)
    r2elems = [x for x in r2elems if not x.isdigit()]
    r1charge = get_charge.get_charge(r1)
    if r1charge > 0:
        p = [r2elems[0], ionic_compound.balance_ion(r1, r2elems[1])]
    else:
        p = [ionic_compound.balance_ion(r2elems[0], r1), r2elems[1]]
    coefs, compounds, summary = equation_matrix.solve([r1, r2], p)
    finalString = f"{coefs[0]} ( {compounds[0]} ) + {coefs[1]} ( {compounds[1]} ) ==> {coefs[2]} ( {compounds[2]} ) + {coefs[3]} ( {compounds[3]} )"
    return finalString

def doubleReplace(r1, r2):
    r1elems = re.findall('[A-Z][^A-Z]*', r1)
    r2elems = re.findall('[A-Z][^A-Z]*', r2)
    p = [ionic_compound.balance_ion(r1elems[0], r2elems[1]), ionic_compound.balance_ion(r2elems[0], r1elems[1])]
    coefs, compounds, summary = equation_matrix.solve([r1, r2], p)
    finalString = f"{coefs[0]} ( {compounds[0]} ) + {coefs[1]} ( {compounds[1]} ) ==> {coefs[2]} ( {compounds[2]} ) + {coefs[3]} ( {compounds[3]} )"
    return finalString
    
def neutralize(saltcat, saltan, acid):
    salt = saltcat + saltan
    r = [salt, acid]
    acidelems = re.findall('[A-Z][^A-Z]*', acid)
    p = [ionic_compound.balance_ion(saltcat, acidelems[1]), "H2O"]
    coefs, compounds, summary = equation_matrix.solve(r, p)
    finalString = f"{coefs[0]} ( {compounds[0]} ) + {coefs[1]} ( {compounds[1]} ) ==> {coefs[2]} ( {compounds[2]} ) + {coefs[3]} ( {compounds[3]} )"
    return finalString

def combust(fuel):
    c = fuel[fuel.index("C") + 1:fuel.index("H")]
    h = fuel[fuel.index("H") + 1:fuel.index("O")]

    if "O" in fuel:
        o = fuel[fuel.index("O") + 1:]
    else:
        o = 0

    if c == "":
        c = 1
    else:
        c = int(c)
    if h == "":
        h = 1
    else:
        h = int(h)
    if o == "":
        o = 1
    else:
        o = int(o)

    coefs = [1, h / 4 + c - o / 2, c, h / 2]
    if (coefs[1]*2)%1!=0:
        coefs = [str(int(x*4)) for x in coefs]
    elif coefs[1]%1!=0:
        coefs = [str(int(x*2)) for x in coefs]
    else:
        coefs = [str(int(x)) for x in coefs]
    
    r = [f"C{str(c)}H{str(h)}O{str(o)}", "O2"]
    p = ["CO2", "H2O"]

    finalString = f"{coefs[0]} ( C{c} H{h} O{o} ) + {coefs[1]} ( O2 ) ==> {coefs[2]} ( CO2 ) + {coefs[3]} ( H2O )"
    summary = eq_summary.summary(coefs, r, p)

    return finalString

def main():
    typ = input("Enter equation: ")
    if typ.lower() == "s":
        r1 = input("Enter the first reactant: ")
        r2 = input("Enter the second reactant: ")
        isIonic = input("Is the product ionic [Y/n]: ")
        isIonic = True if isIonic.lower() == "y" else False 
        print(synthesize(r1, r2, isIonic))
    elif typ.lower() == "d":
        p1 = input("Enter the first product: ")
        p2 = input("Enter the second product: ")
        isIonic = input("Is the reactant ionic [Y/n]: ")
        isIonic = True if isIonic.lower() == "y" else False 
        print(decompose(p1, p2, isIonic))
    elif typ.lower() == "sr":
        r1 = input("Enter substituting reactant: ")
        r2 = input("Enter other reactant: ")
        print(singleReplace(r1, r2))
    elif typ.lower() == "dr":
        r1 = input("Enter first reactant: ")
        r2 = input("Enter second reactant: ")
        print(doubleReplace(r1, r2))
    elif typ.lower() == "n":
        saltcat = input("Enter salt cation: ")
        saltan = input("Enter salt anion: ")
        acid = input("Enter acid: ")
        print(neutralize(saltcat, saltan, acid))
    elif typ.lower() == "c":
        fuel = input("Enter fuel: ")
        print(combust(fuel))
    else: 
        equation_matrix.main()

if __name__ == "__main__":
    main()