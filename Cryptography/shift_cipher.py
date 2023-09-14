ls = [*"abcdefghijklmnopqrstuvwxyz"]

# shifts cyphertext: ct by key: i
def shift(ct, i):
    pt = "".join([ls[(ls.index(c) + i) % 26] for c in ct])
    return pt

def main():
    ct = input().replace(" ", "")
    for i in range(26):
        print(shift(ct, i))

# given cyphertext/ct = "ycvejqwvhqtdtwvwu" and key/i = 24, we get plaintext/pt = "watchoutforbrutus"

if __name__ == "__main__":
    main()