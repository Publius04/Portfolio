import numpy as np
ls = [*"abcdefghijklmnopqrstuvwxyz"]
text = "Herodotus of Halicarnassus here presents his research so that human events do not fade with time. May great and wonderful deeds-some brought forth by the Hellenes, others by the barbarians-not go unsung; as well as the causes that led them to make war on each other."

def encrypt(pt, key):
    n = key.shape[0]
    for i in range(0, len(pt), n):
        if i + n > len(pt):
            block = pt[i, i + n]
        print(block)


def main():
    encrypt(text, np.array([[9, 11], [11, 10]]))
    # key = np.array([[9, 11], [11, 10]])
    # vectors = [np.array([[8, 11]]), np.array([[8, 10]]), np.array([[4, 12]]), np.array([[0, 19]]), np.array([[7, 23]])]
    # for v in vectors:
    #     print([x % 26 for x in list(v.dot(key))])

if __name__ == "__main__":
    main()