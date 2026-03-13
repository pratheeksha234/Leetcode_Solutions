class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_nums = n*(n+1)//2
        actual_num = sum(nums)
        return expected_nums - actual_num
