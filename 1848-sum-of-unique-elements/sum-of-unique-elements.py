class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        rep = []

        for i in range(len(ordered)):
            if ordered[i] in ordered[i + 1:]:
                rep.append(ordered[i])

        return sum([x for x in set(ordered) if x not in rep])


        