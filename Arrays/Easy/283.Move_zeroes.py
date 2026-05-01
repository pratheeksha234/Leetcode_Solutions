class Solution(object):
    def moveZeroes(self, nums):
        ins = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[ins]=nums[i]
                ins+=1
        for i in range(ins, len(nums)):
            nums[i]=0
