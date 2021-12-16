class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_str = (''.join([i for i in s if i.isalnum()])).lower()
        if alpha_str == alpha_str[::-1]:
            return True
        else:
            return False
                     
print(Solution().isPalindrome("1race a car1"))
print(Solution().isPalindrome("1A man, a plan, a canal: Panama1"))
print(Solution().isPalindrome(" "))