class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result1: list[int] = []
        result2: list[int] = []

        for n1 in nums1:
            if n1 in nums2:
                result1.append(n1)

        for n2 in nums2:
            if n2 in nums1:
                result2.append(n2)

        return [len(result1), len(result2)]