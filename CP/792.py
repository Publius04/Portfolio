def fact(k):
    ans = 1
    for i in range(k):
        ans *= i + 1
    return ans

def comb(n, k):
    return fact(n) // (fact(k) * fact(n - k))

def v(n):
    r = 0
    while n % 2**r == 0:
        r += 1
    return r - 1

def S(n):
    S = 0
    for k in range(n):
        S += (-2)**(k + 1) * comb(2*(k + 1), k + 1)
    return S

def u(n):
    return v(3*S(n) + 4)

def U(N):
    U = 0
    for n in range(N):
        U += u((n + 1)**3)
    return U

def main():
    print(U(int(input())))

if __name__ == "__main__":
    main()