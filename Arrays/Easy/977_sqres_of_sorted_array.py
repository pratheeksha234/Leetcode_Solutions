class Solution(object):
    def sortedSquares(self, nums):
        res = []
        for i in nums:
            i*=i
            res.append(i)
        res.sort()
        return res

        
        
