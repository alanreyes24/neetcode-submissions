class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        result = []

        for word in strs:

            sorted_word = ''.join(sorted(word))

            if sorted_word not in seen:

                seen[sorted_word] = [word]

            elif sorted_word in seen:

                seen[sorted_word].append(word)

        for value in seen.values():

            result.append(value)

        return result
            


