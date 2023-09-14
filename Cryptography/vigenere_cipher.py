from itertools import permutations as cb

ls = [*"abcdefghijklmnopqrstuvwxyz"]

def encrypt(pt, k):
    ct = ""
    for i, l in enumerate(pt):
        if l == " ":
            continue
        ct += ls[(ls.index(l) + ls.index(k[i % len(k)])) % 26]
    return ct

def known_plaintext(pt, ct):
    dt = [(ls.index(ct[i]) - ls.index(pt[i])) % 26 if pt[i] != " " else " " for i in range(len(pt))]
    for i in range(len(dt)):
        key_found = False
        for j in range(0, len(dt), i+1):
            if dt[j:j+i+1] != dt[:i+1][:len(dt[j:j+i+1])]:
                key_found = False
                break
            key_found = True
        if key_found:
            key = dt[:i+1]
            break

    if key_found:
        return(key)
    else:
        print("key not found")
        return None
    
def cyphertext_only(plaint, ct, key):
    key_len = 4
    # pt = [ls.index(x) for x in pt]
    ct = [ls.index(x) for x in ct]
    # pt = [ls.index(x) for x in pt]
    self_subtract = [(ct[:-key_len][i] - ct[key_len:][i]) % 26 for i in range(len(ct) - key_len)]
    # print([(pt[:-key_len][i] - pt[key_len:][i]) % 26 for i in range(len(pt) - key_len)])
    for i in list(cb(list(range(26)), key_len)):
        if i[:3] != (19, 7, 4):
            continue
        print(i)
        pt = list(i)
        for j in range(len(self_subtract) - key_len):
            pt.append((pt[j] - self_subtract[j]) % 26)
        print("".join(ls[x] for x in pt))


def main():
    encode = False
    if encode:
        key = input("key: ").lower().replace(" ", "")
        plaintext = input("plaintext: ").lower()
        cyphertext = encrypt(plaintext, key)
        print(cyphertext)
    else:
        # plaintext = input("plaintext: ").lower()
        # cyphertext = input("cyphertext: ").lower()
        # known_plaintext(plaintext, cyphertext)

        # key = known_plaintext("attacking tonight", "ovnlqbpvt eoeqtnh")
        # print("".join(ls[x] if x != " " else " " for x in key))
        cyphertext_only("thequickbrownfoxjumpsoverthelazydog", "EPSDFQQXMZCJYNCKUCACDWJRCBVRWINLOWU".lower(), 0)

if __name__ == "__main__":
    main()

# cucumber -> oehgwgqb