class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result1: int = 0
        result2: int = 0
        set1 = set(nums1)
        set2 = set(nums2)

        for n1 in nums1:
            if n1 in set2:
                result1 += 1

        for n2 in nums2:
            if n2 in set1:
                result2 += 1

        return [result1, result2]

        return [len(result1), len(result2)]