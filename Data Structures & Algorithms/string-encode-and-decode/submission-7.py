class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for string in strs:

            string_length = len(string)

            encoded_string += str(string_length)
            encoded_string += "#"

            for char in string:

                encoded_string += (char)

        return encoded_string


    def decode(self, s: str) -> List[str]:

        if len(s) == 0:

            return []

        result = []
        position = 0
        total_length = len(s)

        while position < total_length:

            length_str = ""

            while s[position] != "#":

                length_str += s[position]
                position += 1

            length = int(length_str)

            position += 1  # skip the "#"

            word = s[position:position + length]
            result.append(word)

            position += length

        return result