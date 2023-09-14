#Larry: rm number called in the longest time
#Robin: rm number in mem longest

import random

def game(round_cap, seed):
    lmem = []
    rmem = []
    lscore = 0
    rscore = 0
    random.seed(seed)
    for i in range(round_cap):
        num = random.randint(1, 10)
        if num in lmem:
            lscore += 1
            lmem.remove(num)
            lmem.insert(0, num)
        else:
            lmem.insert(0, num)
            if len(lmem) == 6:
                lmem.pop()

        if num in rmem:
            rscore += 1
        else:
            rmem.insert(0, num)
            if len(rmem) == 6:
                rmem.pop()
    return lscore, rscore 

def main():
    ltot = 0
    rtot = 0
    i = 1
    while True:
        tots = game(50, i)
        ltot += tots[0]
        rtot += tots[1]
        
        print(f"{ltot/i} : {rtot/i}")
        i += 1
main()
