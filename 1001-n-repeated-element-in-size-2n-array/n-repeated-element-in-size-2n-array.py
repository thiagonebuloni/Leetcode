class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        set1 = set(sorted(nums))
        repeated_nums = {x: 0 for x in set1}
        
        for x in nums:
            repeated_nums[x] += 1

        return max(repeated_nums, key=repeated_nums.get)