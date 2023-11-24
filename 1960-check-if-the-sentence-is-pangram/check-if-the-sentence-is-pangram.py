class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet: list[str] = string.ascii_lowercase
        for letter in alphabet:
            if letter not in sentence:
                return False
        return True