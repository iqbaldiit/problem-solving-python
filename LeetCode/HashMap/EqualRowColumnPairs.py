# Source: https://leetcode.com/problems/equal-row-and-column-pairs/solutions/6441096/best-simple-solution-beats-93-59-by-iqba-w0d3/
'''
    Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
    such that row ri and column cj are equal.
    A row and column pair is considered equal if they contain the same elements in 
    the same order (i.e., an equal array).

    Example 1:


    Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
    Output: 1
    Explanation: There is 1 equal row and column pair:
    - (Row 2, Column 1): [2,7,7]
    Example 2:


    Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    Output: 3
    Explanation: There are 3 equal row and column pairs:
    - (Row 0, Column 0): [3,1,2,2]
    - (Row 2, Column 2): [2,4,2,2]
    - (Row 3, Column 2): [2,4,2,2]


    Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 200
    1 <= grid[i][j] <= 105
'''
# Solution
def equalPairs(grid: list[list[int]]) -> int:
    ### Approach 1
    # n=len(grid)
    # count=0
    # for i in range(n):
    #     for j in range(n):
    #         isEqual=True
    #         for k in range(n):
    #             if(grid[i][k]!=grid[k][j]):
    #                 isEqual=False
    #                 break
    #         if (isEqual):
    #             count+=1

    ### Approach: 2
    # from collections import defaultdict
    
    # dicRowCount = defaultdict(int)  # Create a dictionary to count occurrences of each row
    # nCount = 0  # Initialize the count of equal row-column pairs

    # # Step 1: Count occurrences of each row
    # for row in grid:
    #     dicRowCount[tuple(row)] += 1  # Convert the row to a tuple (hashable) and count it
    
    # # Step 2: Check if each column matches any row
    # for column in zip(*grid):  # Use zip(*grid) to get columns        
    #     nCount += dicRowCount[column]  # Add the count of matching rows

    # return nCount  # Return the total count of equal row-column pairs

    ### Approach: 3
    from collections import Counter
    dicRowCount=Counter(tuple(row) for row in grid) # Count each row in the grid
    # convert column into by zip 
    # match with rows of grid
    # sum each count if match and return
    return sum(dicRowCount[column] for column in zip(*grid))
    
    


# Execution
print(equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]])) # Output: 1
print(equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])) # Output: 3