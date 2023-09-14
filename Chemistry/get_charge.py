import json, re

stream = open("ptable.json")
ptable = json.load(stream)
stream.close()

def get_charge(compound):
    compoundsplit = re.findall('[A-Z][^A-Z]*', compound)
    charge = 0
    for item in compoundsplit:
        symbol = ""
        num = ""
        for char in item:
            if not char.isdigit():
                symbol += char.lower()
            else:
                num += char 
        if num == "":
            num = '1'
        potcharges = eval(ptable[symbol.title()]["charges"])
        if len(potcharges) == 1:
            charge += int(potcharges[0]) * int(num)
        else:
            tmp = int(input("Multiple charges found for " + symbol + ":\n" + str(potcharges) + "\nEnter desired charge: "))
            if tmp not in potcharges:
                print("Not part of given potential charges.")
            charge += tmp * int(num)
    return charge

def main():
    compound = input("Enter compound: ")
    charge = get_charge(compound)
    print(charge)

if __name__ == "__main__":
    main()