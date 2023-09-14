def solve(time, inter):
    t1 = time
    t2 = 

def main():
    n = int(input())
    ans = []
    for _ in range(n):
        inp = input().split(" ")
        time = inp[0].split(":")
        inter = int(inp[1])
        ans.append(solve(time, inter))

    for a in ans:
        print(a)

if __name__ == "__main__":
    main()
