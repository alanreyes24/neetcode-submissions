class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ''.join(char for char in s.lower() if char.isalnum())
        left = 0
        right = len(cleaned) - 1

        while left < right:

            print(cleaned)

            if cleaned[left] == cleaned[right]:

                left += 1
                right -= 1
            
            else:

                return False

        return True