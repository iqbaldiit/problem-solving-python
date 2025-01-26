'''
        You have a long flowerbed in which some of the plots are planted, and some are not. However, 
        flowers cannot be planted in adjacent plots.

        Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
        and an integer n, return true if n new flowers can be planted in the flowerbed without violating 
        the no-adjacent-flowers rule and false otherwise. 

        Example 1:

        Input: flowerbed = [1,0,0,0,1], n = 1
        Output: true
        Example 2:

        Input: flowerbed = [1,0,0,0,1], n = 2
        Output: false
 

        Constraints:

        1 <= flowerbed.length <= 2 * 104
        flowerbed[i] is 0 or 1.
        There are no two adjacent flowers in flowerbed.
        0 <= n <= flowerbed.length
'''

'''
    Input: flowerbed = [1, 0, 0, 0, 1], and n = 1 (Number of flowers)
    Output: true   
    Explanation: It means You can plant 1 flower in the middle position (index 2), resulting in [1, 0, 1, 0, 1]. 
                    The flower where you want to plant, the previous and next must be blanked.
'''

# Solution canPlaceFlowers
def Plant(flowerbed:list[int],  n:int)->bool:
    nFlowerPlanted = 0
    nNumberOfExistingPlace = len(flowerbed)

    for i in range(nNumberOfExistingPlace):
        if (flowerbed[i] == 0):
            # check in the previous place is first or, flower planted or not
            bPreviousPlace = 0 if i==0 else flowerbed[i-1] 
            #Check the next place, flower planted or not
            bNextPlace = 0 if (i == nNumberOfExistingPlace -1) else flowerbed[i + 1]

            if (bPreviousPlace ==0 and bNextPlace == 0):
                flowerbed[i]=1
                nFlowerPlanted+=1
                i+=1                


    return (nFlowerPlanted>=n)


# Execution
# Inputs:
flowerbed = [1, 0, 0, 0, 0, 1]
n = 2

# invoke function
print(Plant(flowerbed,n))
