class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter_dict = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                       "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        encode = set()
        for word in words:
            encode_word = ''
            for char in word:
                encode_char = letter_dict[ord(char) - ord('a')]
                encode_word += encode_char
            encode.add(encode_word)
        return encode.__len__()


solution = Solution()
# ret = solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
# ret = solution.uniqueMorseRepresentations(["gin"])
# ret = solution.uniqueMorseRepresentations([""])
# ret = solution.uniqueMorseRepresentations([])
ret = solution.uniqueMorseRepresentations(["", "", ""])
print(ret)
