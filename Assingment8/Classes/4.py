class PairFinder:
    def find_pair(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return (lookup[complement], i)
            lookup[num] = i
