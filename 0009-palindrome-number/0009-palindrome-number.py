class Solution:
    def isPalindrome(self, x: int) -> bool:

        string_num = f"{x}"
        
        for i in range(0, len(string_num) // 2): 
            if string_num[i] != string_num[len(string_num) - i - 1]: 
                return False
             
        return True