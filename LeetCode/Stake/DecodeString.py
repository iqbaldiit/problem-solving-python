# Source: https://leetcode.com/problems/decode-string/solutions/6473799/best-simple-solution-beats-100-and-55-by-9n3h/
'''
     Given an encoded string, return its decoded string.
     The encoding rule is: k[encoded_string], where the encoded_string inside the square 
     brackets is being repeated exactly k times. Note that k is guaranteed to be a 
     positive integer.
    
    You may assume that the input string is always valid; there are no extra white spaces, 
     square brackets are well-formed, etc. Furthermore, you may assume that the original 
     data does not contain any digits and that digits are only for those repeat numbers, 
     k. For example, there will not be input like 3a or 2[4].
     
    The test cases are generated so that the length of the output will never exceed 105.

    Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

    Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
 

        Constraints:
        1 <= s.length <= 30
        s consists of lowercase English letters, digits, and square brackets '[]'.
        s is guaranteed to be a valid input.
        All the integers in s are in the range [1, 300].
'''
# Solution
def decodeString(s: str) -> str:
    count_stack = []
    string_stack = []
    current_string = []
    k = 0

    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)
        elif ch == '[':
            count_stack.append(k)
            string_stack.append(current_string)
            current_string = []
            k = 0
        elif ch == ']':
            decoded_string = string_stack.pop()
            current_k = count_stack.pop()
            current_string = decoded_string + current_string * current_k
        else:
            current_string.append(ch)

    return ''.join(current_string)

# Execution
print(decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(decodeString("3[a2[c]]"))  # Output: "accaccacc"
print(decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
