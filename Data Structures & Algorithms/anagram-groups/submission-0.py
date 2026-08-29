class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = {}
        result = []

        for string in strs:

            sorted_string = ''.join(sorted(string))
            
            if sorted_string not in hash:

                hash[sorted_string] = [string]
            
            elif sorted_string in hash:

                hash[sorted_string].append(string)

        for value in hash.values():
            result.append(value)
            
        return result