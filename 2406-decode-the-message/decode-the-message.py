class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        decoded = ""

        unique_set = set()
        unique_key = ""
        key = key.replace(" ", "")
        for char in key:
            if char not in unique_set:
                unique_set.add(char)
                unique_key += char

        for char in message:
            if char != " ":
                idx = unique_key.index(char)
                decoded += alphabet[idx]
            else:
                decoded += " "
        return decoded