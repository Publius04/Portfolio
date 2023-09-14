# Given an array of ints nums, give all triplets [num[i], num[j], num[k]] such that i, j, and k are distinct and num[i] + num[j] + num[k] == 0

# [-1, 0, 1, 2, -1, -4]

class Solution:
    def __init__(self, nums):
        self.nums = sorted(nums)
        self.z = self.nums.index(0) if 0 in self.nums else -1
        self.trips = []

    def _twoSum(self, target):
        hashmap = {}
        for i in range(len(self.nums)):
            complement = -target - self.nums[i]
            if complement in hashmap and -complement not in hashmap and complement != -target:
                return [self.nums[i], complement, target]
            hashmap[self.nums[i]] = i
        return -1

    def solve(self):
        for i in range(len(self.nums)):
            ids = self._twoSum(self.nums[i])
            if ids != -1:
                self.trips.append(ids)
        print(self.trips)

nums = eval(input())
sol = Solution(nums)
sol.solve()