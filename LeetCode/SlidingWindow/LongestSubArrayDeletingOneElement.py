# Source: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/6410922/simple-best-solution/
'''
        Given a binary array nums, you should delete one element from it.
        Return the size of the longest non-empty subarray containing only 1's in 
        the resulting array. Return 0 if there is no such subarray.

        Example 1:
        Input: nums = [1,1,0,1]
        Output: 3
        Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
        
        Example 2:
        Input: nums = [0,1,1,1,0,1,1,0,1]
        Output: 5
        Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
        
        Example 3:
        Input: nums = [1,1,1]
        Output: 2
        Explanation: You must delete one element.

        Constraints:

        1 <= nums.length <= 105
        nums[i] is either 0 or 1. 
'''
def longest_subarray(self, nums):
    nLeft = 0
    nMax_len = 0
    nZero_count = 0

    for nRight in range(len(nums)):
        if nums[nRight] == 0:
            nZero_count += 1

        while nZero_count > 1:
            if nums[nLeft] == 0:
                nZero_count -= 1
            nLeft += 1

        nMax_len = max(nMax_len, nRight - nLeft)

    return nMax_len