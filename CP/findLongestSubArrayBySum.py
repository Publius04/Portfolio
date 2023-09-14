def findSubArray(array, s):
    l, r = 0, 1
    ans = [0, []]
    if len(array) == 1:
        return array[0]

    while r <= len(array):
        if sum(array[l:r]) < s or r == l:
            r += 1
        else:
            l += 1
        if sum(array[l:r]) == s:
            ans = [max(ans[0], len(array[l:r])), [l, r]]
    ans = [ans[1][0] + 1, ans[1][1]]
    return ans

def main():
    ls = [1, 2, 3, 4, 5, 1, 6, 78]
    s = 5
    print(findSubArray(ls, s))

main()