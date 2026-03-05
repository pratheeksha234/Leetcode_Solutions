class Solution(object):
    def removeDuplicates(self, nums):
        seen = set()
        k = 0  # position to place unique elements

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[k] = nums[i]
                k += 1

        return k
