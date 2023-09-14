import get_mass    

def main():
    compound = input("Enter compound: ")
    grams = float(input("Enter grams: "))
    mass = get_mass.get_mass(compound)
    print(grams / mass)

if __name__ == "__main__":
    main()