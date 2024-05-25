class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        resultado = 0
        for idx in range(len(s)):
            x = s[idx]
            y = t.index(s[idx])
            resultado += abs(idx - y)
        return resultado