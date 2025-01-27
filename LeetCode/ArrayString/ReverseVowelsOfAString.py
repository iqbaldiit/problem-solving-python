
# Source: https://leetcode.com/problems/reverse-vowels-of-a-string/solutions/6333846/simple-best-solution-with-using-two-poin-se3g/
'''
        Given a string s, reverse only all the vowels in the string and return it.
        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

        Example 1:
        Input: s = "IceCreAm"
        Output: "AceCreIm"

        Explanation:
        The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

        Example 2:
        Input: s = "leetcode"
        Output: "leotcede"

        Constraints:

        1 <= s.length <= 3 * 105
        s consist of printable ASCII characters.
'''

def ReverseVowels(s:str)->str:
    # set the vowels
    vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]
    aryStr=list(s)
    left=0
    right=len(aryStr)-1

    # Two-pointer approach to reverse vowels in place
    # It means left pointer move ahed untill found vowel
    # And right pointer move back untill found vowel

    while left<right:
        # Move left pointer until a vowel is found
        
        while left<right and aryStr[left] not in vowels:
            left+=1
        # Move back right pointer until a vowel is found
        
        while left<right and aryStr[right] not in vowels:
            right-=1    

        # Swap the vowels
        if left<right:
            aryStr[left], aryStr[right] = aryStr[right], aryStr[left]
            left+=1 
            right-=1  

    return ''.join(aryStr)     


# Executions
#inputs
inputs = "IceCreAm"
#invoke functions
print(ReverseVowels(inputs))

    

         