import time
from math import floor
import random

TEST = False

def get_match(n, num):
	m = 10 ** (n - 1)
	mcurr = floor(len(str(num + m)) / 2)
	for curr in range(mcurr):
		tot = num + m
		l = int(str(tot)[curr])
		r = int(str(tot)[len(str(tot)) - 1 - curr])
		#print(f"l: {l}, r: {r}")
		if l != r:
			m += ((l - r) % 10) * (10 ** curr)
			#print(f"m = {m}")
			if len(str(tot)) % 2 == 0 and curr == mcurr - 1 and l < r:
				m += 10 ** (len(str(tot)) / 2 - 1)
			elif curr == mcurr - 1 and int(str(tot)[int((len(str(tot)) - 1) / 2) + 1]) + int(str(m)[int((len(str(tot)) - 1) / 2) + 1]) >= 10:
				m += 10 ** ((len(str(tot)) - 1) / 2 - 1)
		#print(f"m = {m}")
	return(int(m))

def main():
    t = int(input())
    ans = []
    for i in range(t):
        n = int(input())
        num = int(input())
        ans.append(get_match(n, num))
    for a in ans:
        print(a)

if TEST:
	l = random.sample(range(0, 10000), 100)
	for n in l:
		m = get_match(len(str(n)), n)
		print(f"m: {m}, n + m: {n + m}")
		time.sleep(0.4)
else:
	main()
