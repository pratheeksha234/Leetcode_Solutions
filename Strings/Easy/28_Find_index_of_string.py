class Solution(object):
    def strStr(self, haystack, needle):
        for ch in range(len(haystack)-len(needle)+1):
            new = haystack[ch : ch + len(needle)]
            if new == needle:
                return ch
        return -1
