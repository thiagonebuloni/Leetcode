class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        elif x < 10:
            return True

        reverseNum = 0
        tempOriginal = x

        while (tempOriginal > 1):
            lastDigit = tempOriginal % 10
            print(lastDigit)
            reverseNum = int(reverseNum) * 10 + int(lastDigit)
            tempOriginal = tempOriginal / 10

        if (x == int(reverseNum)):
            return True
        else:
            return False