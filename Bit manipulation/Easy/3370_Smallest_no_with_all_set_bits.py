class Solution(object):
    def smallestNumber(self, n):
        a = bin(n)[2:]
        length = len(a)
        result = ""
        for i in range(length):
            result += "1"
        x = int(result, 2)
        return x
            
