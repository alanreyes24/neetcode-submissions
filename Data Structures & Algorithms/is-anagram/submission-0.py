class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        counter = dict()

        for letter in s:

            counter[letter] = counter.get(letter, 0) + 1

        for letter in t:

            counter[letter] = counter.get(letter, 0) - 1

        for value in counter.values():
            
            if value != 0:
                return False

        return True