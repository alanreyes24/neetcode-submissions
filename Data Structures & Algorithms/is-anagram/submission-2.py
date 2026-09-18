class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):

            return False

        seen = {}

        for letter in s:

            seen[letter] = seen.get(letter, 0) + 1

        for letter in t:

            if letter in seen:
                
                seen[letter] -= 1

            else:

                return False

            if seen[letter] < 0:
                return False

        for values in seen.values():

            if values != 0:

                return False
    
        return True

        