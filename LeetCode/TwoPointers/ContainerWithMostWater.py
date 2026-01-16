# Source: https://leetcode.com/problems/container-with-most-water/solutions/6377662/simple-best-solution-by-iqbaldiit-ty63/
'''
       You are given an integer array height of length n. 
       There are n vertical lines drawn such that the two endpoints of 
       the ith line are (i, 0) and (i, height[i]).

       Find two lines that together with the x-axis form a container, 
       such that the container contains the most water.

       Return the maximum amount of water a container can store.

       Notice that you may not slant the container.

       Example 1:


       Input: height = [1,8,6,2,5,4,8,3,7]
       Output: 49
       Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
       Example 2:
       

       Input: height = [1,1]
       Output: 1


       Constraints:

       n == height.length
       2 <= n <= 105
       0 <= height[i] <= 104 
'''
# Solution
def maxArea(height: list[int]) -> int:    
    nLeft,nRight=0,len(height)-1 # Two pointer
    nMaxArea=0

    while(nLeft<nRight):
        nWidth=nRight-nLeft
        nMinHeight=min(height[nLeft],height[nRight])
        nMaxArea=max(nMaxArea,nMinHeight*nWidth)

        if height[nLeft]<height[nRight]:
            nLeft+=1
        else:
            nRight-=1
    return nMaxArea


# Execution
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))# Output: 49
print(maxArea([1, 8, 6, 2]))# Output: 6
print(maxArea([1, 7, 8, 6, 2, 5, 4, 8, 3]))# Output: 42
print(maxArea([1, 1]))# Output: 1