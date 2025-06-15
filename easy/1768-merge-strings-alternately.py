# Problem: Merge Strings Alternately
# URL: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy
# Tags: array, string

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 24 ms | Beats 99.28%
        # 17.59 MB | Beats 94.48%
        # O(n + m)
        min_len = min(len(word1), len(word2))
        merged = []
        for index in range(min_len):
            merged.append(word1[index] + word2[index])
        if len(word1) > len(word2): 
            merged.append(word1[min_len:])
        else:
            merged.append(word2[min_len:])
        return "".join(merged)

