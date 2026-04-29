class Solution(object):
    def check(self, nums):
        count = 0
        n = len(nums)
        for i in range(n):
            next_index = (i + 1) % n
            if nums[i] > nums[next_index]:
                count += 1
        if count>1:
            return False
        return count <= 1   
