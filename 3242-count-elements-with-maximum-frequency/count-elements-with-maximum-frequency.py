class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_frequencies = {x: 0 for x in nums}

        for num in nums:
            max_frequencies[num] += 1
        maximum = max(max_frequencies.values())
        soma = 0
        for num in max_frequencies.values():
            if num == maximum:
                soma += num
        return soma