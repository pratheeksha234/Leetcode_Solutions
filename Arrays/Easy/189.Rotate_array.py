class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        new = 0
        k = k % n
        while new<k:
            val = nums.pop()
            nums.insert(0, val)
            new+=1
        return nums
