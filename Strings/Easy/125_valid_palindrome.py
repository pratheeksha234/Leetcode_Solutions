class Solution(object):
    def isPalindrome(self, s):
        letters = []
        s = s.lower()
        for ch in s:
            if ch.isalnum():
                letters.append(ch)

        return letters[::]==letters[::-1]
