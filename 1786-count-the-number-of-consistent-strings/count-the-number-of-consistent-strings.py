class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        not_in: int = 0

        for word in words:
            for letter in word:
                if letter not in allowed: 
                    not_in += 1
                    break
            
        return len(words) - not_in