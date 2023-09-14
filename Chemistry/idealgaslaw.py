lterms = ["p", "v"]
rterms = ["n", "t"]
R = 0.08206

def main():

    constants = input("Enter constants: ").lower().split(" ")
    for c in constants:
        if c in lterms:
            lterms.remove(c)
        if c in rterms:
            rterms.remove(c)
 
    ans = 1
    
    for l in lterms:
        lval = float(input(f"Enter {l} vallue: "))
        ans *= lval
    for r in rterms:
        rval = float(input(f"Enter {r} value: "))
        ans /= rval
    
    print(ans/R)

if __name__ == "__main__":
    main()