# Source: https://leetcode.com/problems/maximum-average-subarray-i/solutions/6387663/simple-best-solution-by-iqbaldiit-a4uy/
'''
    You are given an integer array nums consisting of n elements, 
    and an integer k.
    Find a contiguous subarray whose length is equal to k 
    that has the maximum average value and return this value. 
    Any answer with a calculation error less than 10-5 will 
    be accepted. 

    Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
    
    Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000

    Constraints:
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104
'''
# Solution
def findMaxAverage( nums: list[int], k: int) -> float:
    # Compute the sum of the first k elements
    max_sum = sum(nums[:k])
    current_sum = max_sum

    # Use a sliding window to compute the sum of subsequent subarrays
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    # Compute the maximum average
    return max_sum/k  

# Execution   
print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([5],1))