# Source: https://leetcode.com/problems/product-of-array-except-self/solutions/6342729/simple-best-solution-by-iqbaldiit-6m7w/
'''
        Given an integer array nums, return an array answer such that answer[i] 
        is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation.

 

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
 

    Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
'''

def productExceptSelf(nums):
    n=len(nums)
    ans=[1]*n # initialize the array with 1st element

    # Step1: Calculate prefix product
    for i in range(1,n):
        ans[i]=ans[i-1]*nums[i-1]
    
    # Step2: Calculate suffix products and multiply with prefix products
    nSuffixProduct=1 # Initialize suffix product
    for i in range(n-1,-1,-1):
        ans[i]*=nSuffixProduct # Multiply prefix product with suffix product
        nSuffixProduct*=nums[i] # Update suffix product for the next iteration

    return ans


# Execution
# Inputs
aryInput = [1, 2, 3, 4]
result = productExceptSelf(aryInput)
print(result)  # Output: [24, 12, 8, 6]