class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result: int = 0
        alloweds: list = list(allowed)
        print(words)
        for word in words:
            new_word = ""
            for letter in word:
                if letter in alloweds:
                     new_word += letter
                     
                if letter not in alloweds:
                    print(f"{letter} from {word} not in {alloweds}")
                    break
            print(f"{word} in alloweds")
            if new_word == word: 
                result += 1
        return result
