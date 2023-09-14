ls = [*"abcdefghijklmnopqrstuvwxyz"]

def charencode(text):
    return [ls.index(x) for x in text]    

def chardecode(array):
    return "".join([ls[int(x)] for x in array])

def main():
    encode = input()
    if encode != "":
        array = input().replace(" ", "").split(",")
        print(chardecode(array))
    else:
        text = input().replace(" ", "").lower()
        print(charencode(text))

if __name__ == "__main__":
    main()

# [12, 10, 5, 12, 10, 5, 12, 10]

# m = 3, k = (12, 10, 5)

5 * np.array([[10, -11], [-11, 9]])
