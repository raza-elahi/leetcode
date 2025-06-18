# Problem: Longest Palindromic Substring
# URL: https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty: Medium
# Tags: two pointers, string, dynamic programming

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force
        # 7988 ms | Beats 7.79%
        # 18.45 MB | Beats 18.29%
        bank = {}

        item_count = len(s)
        for i in range(item_count):
            for j in range(i + 1, item_count + 1):
                if j - i in bank:
                    continue
                substr = s[i:j]
                if substr == substr[::-1]:
                    bank[len(substr)] = substr

        return bank[max(bank.keys())]

    def longestPalindrome(self, s: str) -> str:
        # center expansion
        # 225 ms | Beats 84.35%
        # 17.68 MB | Beats 96.19%
        def expand(t, l, r):
            while l >= 0 and r < len(t) and t[l] == t[r]:
                l -= 1
                r += 1
            return t[l + 1:r]

        ans = ""

        for i in range(len(s)):
            odd_search = expand(s, i, i)
            even_search = expand(s, i, i + 1)

            ans = max([odd_search, even_search, ans], key=len)

        return ans

