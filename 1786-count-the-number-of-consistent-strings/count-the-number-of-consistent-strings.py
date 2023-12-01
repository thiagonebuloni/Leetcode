class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        n: int = 0

        for w in words:
            for l in w:
                if l not in allowed: 
                    n += 1
                    break
            
        return len(words) - n