# Source: 
'''
    Given a binary array nums and an integer k, return the maximum number of 
    consecutive 1's in the array if you can flip at most k 0's.

    Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

    Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


    Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length
'''
def longestOnes(nums, k):
    nLeft = 0  # Left pointer of the window
    nZero_count = 0  # Count of 0's in the current window
    nMax_length = 0  # Maximum length of the window

    for right in range(len(nums)):
        # If the current element is 0, increment zero_count
        if nums[right] == 0:
            nZero_count += 1

        # If zero_count exceeds k, shrink the window from the left
        while nZero_count > k:
            if nums[nLeft] == 0:
                nZero_count -= 1
            nLeft += 1

        # Update the maximum window size
        nMax_length = max(nMax_length, right - nLeft + 1)

    return nMax_length

# Execution
print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # Output: 6
print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))  # Output: 10