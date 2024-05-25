class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        score = 0
        for idx, char in enumerate(s):
            score += abs(t.find(char)-idx)
        return score