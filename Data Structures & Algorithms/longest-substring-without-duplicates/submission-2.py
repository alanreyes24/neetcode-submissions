class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        if len(s) == 0:

            return 0

        start = 0
        end = 1
        highest = 1

        seen.add(s[start])
        while end < len(s):

            if s[end] not in seen:

                

                seen.add(s[end])
                end += 1
            
            elif s[end] in seen:

                while s[start] != s[end]:

                    seen.discard(s[start])
                    start += 1
                
                start += 1
                end += 1
            
            if len(seen) > highest:

                highest = len(seen)

        
        print(seen)
        return highest
        