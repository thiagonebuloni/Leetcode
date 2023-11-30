class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        length: int = len(words)
        result: int = 0

        for i in range(length):
            for j in range(i + 1, length):
                if words[i] == words[j][::-1]:
                    result += 1
        
        return result