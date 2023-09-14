import re, json

def get_mass(compound):
    with open("ptable.json", "r") as ptablejson:
        ptable = json.load(ptablejson)
        list = re.findall('[A-Z][^A-Z]*', compound)
        tot = 0
        for item in list:
            symbol = ""
            num = ""
            for char in item:
                if not char.isdigit():
                    symbol += char.lower()
                else:
                    num += char 
            if num == "":
                num = '1'
            tot += int(num) * float(ptable[symbol.title()]["weight"])
    return tot

def main():
    compound = input("Enter compound: ")
    mass = get_mass(compound)
    print(mass)
    
if __name__ == "__main__":
    main()
