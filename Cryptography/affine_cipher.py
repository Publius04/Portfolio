from math import gcd
ls = [*"abcdefghijklmnopqrstuvwxyz"]

# A function that returns a number's multiplicative inverse
def mi(n, m):
    if gcd(n, m) != 1:
        return None
    
    for i in range(m):
        if (n * (i + 1)) % m == 1:
            return i + 1

# an encryption function for affine cyphers, pt: string of plaintext, k: list of length-2 [a, b]
def encrypt(pt, k):
    ct = "".join([ls[(k[0] * ls.index(c) + k[1]) % 26] for c in pt])

    # here is the same code written more clearly
    # ct = ""
    # for c in pt:
    #     # this line follows the form: y = (a * x + b) mod 26
    #     y = (k[0] * ls.index(c) + k[1]) % 26
    #     ct += ls[y]

    return ct

# an decryption function for affine cyphers, ct: string of cyphertext, k: list of length-2 [a, b]
def decrypt(ct, k):
    pt = "".join([ls[(mi(k[0], 26) * (ls.index(c) - k[1])) % 26] for c in ct])

    # here is the same code written more clearly
    # pt = ""
    # for c in ct:
    #     # this line follows the form: x = a^-1 * (y - b) mod 26
    #     x = (mi(k[0], 26) * (ls.index(c) - k[1])) % 26
    #     pt += x

    return pt

def main():
    affine = decrypt("edsgickxhuklzveqzvkxwkzukcvuh", [9, 10])
    print(affine) # which gives: "ifyoucanreadthisthankateacher"

if __name__ == "__main__":
    main()