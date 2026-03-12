class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0

        for ch in range(len(s) - 1, -1, -1):
            if s[ch] == " " and count == 0:
                continue
            if s[ch] == " " and count > 0:
                return count
            count += 1

        return count
