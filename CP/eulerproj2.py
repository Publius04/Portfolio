import math

def arith_deriv(factors):
    num = 1
    for f in factors:
        num *= f
    if len(factors) <= 1:
        return 1
    else:
        last = factors.pop()
        ans = num / last + last * arith_deriv(get_factors(int(num / last)))
        return int(ans)

def get_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num = num / 2
    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num = num / i
    if num > 2:
        factors.append(num)
    return factors

def special_gcd(num):
    ans = math.gcd(num, arith_deriv(get_factors(num)))
    return ans

def dif_func(set):
    difs = []
    for i in range(len(set)) - 1:
        difs.append(set[i + 1] - set[i])
    return difs 

def main():
    sum = 0
    sumset = []
    for i in range(int(5e8)):
        tmp = special_gcd(i + 1)
        sum += tmp
        sumset.append(tmp)
    print(sum, ":", get_factors(sum))
    #return sum, sumset

#ans, ansset = main()
#print(ans)
main()
