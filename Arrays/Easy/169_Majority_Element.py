# Approach: Sorting
# The array is sorted first. Since the majority element appears more than n//2 times,
# it will always occupy the middle position of the sorted array.
# Therefore, returning nums[len(nums)//2] guarantees the majority element.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) since sorting is done in-place
#
# This is a simple and clean approach that works efficiently for this problem.

class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
