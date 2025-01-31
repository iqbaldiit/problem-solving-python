
#Source: https://leetcode.com/problems/string-compression/solutions/6351745/simple-best-solution-by-iqbaldiit-c8bn/
'''
       Given an array of characters chars, compress it using the following algorithm:

       Begin with an empty string s. For each group of consecutive repeating characters in chars:

       If the group's length is 1, append the character to s.
       Otherwise, append the character followed by the group's length.
       The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

       After you are done modifying the input array, return the new length of the array.

       You must write an algorithm that uses only constant extra space.



       Example 1:

       Input: chars = ["a","a","b","b","c","c","c"]
       Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
       Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
       Example 2:

       Input: chars = ["a"]
       Output: Return 1, and the first character of the input array should be: ["a"]
       Explanation: The only group is "a", which remains uncompressed since it's a single character.
       Example 3:

       Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
       Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
       Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


       Constraints:

       1 <= chars.length <= 2000
       chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.     
     
'''
# Solution
def compress(chars)->int:
    read=0 # Pointer to read original array
    write=0 # Pointer to write compressed array

    while(read<len(chars)):
        currentChar=chars[read]
        nCount=0

        # Count the number of consecutive repeating characters
        while(read<len(chars) and chars[read]==currentChar):
            nCount+=1
            read+=1

        # Write the compressed char
        chars[write]=currentChar
        write+=1

        # Write count if greater than 1
        if nCount>1:
            for n in str(nCount):
                chars[write]=n
                write+=1
    return write


# Execution
print(compress(["a","a","b","b","c","c","c"]))# Output: 6
print(compress(["a"]))# Output: 1
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))# Output: 4


