class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        count = 0
        length = len(nums)

        for i in range(length):
            for j in range(length):
                if i < j and abs(nums[i] - nums[j]) == k:
                    count += 1
        return count