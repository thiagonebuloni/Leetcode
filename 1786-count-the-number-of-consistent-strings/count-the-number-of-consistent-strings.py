class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result: int = 0
        alloweds: list = list(allowed)
        for word in words:
            new_word = ""
            for letter in word:
                if letter in alloweds:
                     new_word += letter
                     
                if letter not in alloweds:
                    break
            if new_word == word: 
                result += 1
        return result
