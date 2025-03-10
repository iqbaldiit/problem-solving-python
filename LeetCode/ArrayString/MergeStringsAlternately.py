'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string. 
Return the merged string. 
Example 1: Input: word1 = "abc", word2 = "pqr" Output: "apbqcr" 
Explanation: The merged string will be merged as so: word1: a b c word2: p q r merged: a p b q c r 

Example 2: Input: word1 = "ab", word2 = "pqrs" Output: "apbqrs" 
Explanation: Notice that as word2 is longer, "rs" is appended to the end. word1: a b word2: p q r s merged: a p b q r s 

Example 3: Input: word1 = "abcd", word2 = "pq" Output: "apbqcd" 
Explanation: Notice that as word1 is longer, "cd" is appended to the end. 
word1: a b c d word2: p q merged: a p b q c d 

Constraints: 1 <= word1.length, word2.length <= 100 word1 and word2 consist of lowercase English letters.
'''

def merge_alternately(word1, word2):
    merged_string = []
    i, j = 0, 0

    # Loop through both strings until we reach the end of one of them
    while i < len(word1) and j < len(word2):
        merged_string.append(word1[i])
        merged_string.append(word2[j])
        i += 1
        j += 1

    # If word1 is longer, append the remaining characters
    while i < len(word1):
        merged_string.append(word1[i])
        i += 1

    # If word2 is longer, append the remaining characters
    while j < len(word2):
        merged_string.append(word2[j])
        j += 1

    return ''.join(merged_string)

# Example usage
print(merge_alternately("abc", "pqr"))   # Output: "apbqcr"
print(merge_alternately("ab", "pqrs"))   # Output: "apbqrs"
print(merge_alternately("abcd", "pq"))   # Output: "apbqcd"
