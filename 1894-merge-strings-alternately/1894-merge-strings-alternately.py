class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1),len(word2))
        mix = []

        for i in range(max_len):
            if i < len(word1):
                mix.append(word1[i])
            if i < len(word2):
                mix.append(word2[i])

        return "".join(mix)
