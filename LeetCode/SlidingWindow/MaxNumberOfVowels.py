# Source: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/solutions/6396326/simple-best-solution/
'''
    Given a string s and an integer k, return the maximum number of 
    vowel letters in any substring of s with length k.
    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

    Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

    Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

    Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.


    Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    1 <= k <= s.length
'''

def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowels = 0
    current_vowels = 0

    # Calculate the number of vowels in the first window
    for i in range(k):
        if s[i] in vowels:
            current_vowels += 1
    max_vowels = current_vowels

    # Slide the window across the string
    for i in range(k, len(s)):
        if s[i] in vowels:
            current_vowels += 1
        if s[i - k] in vowels:
            current_vowels -= 1
        max_vowels = max(max_vowels, current_vowels)

    return max_vowels    


# Execution
print(maxVowels('abciiidef', 3))  # Output: 3
print(maxVowels('aeiou', 2))  # Output: 2
print(maxVowels('leetcode', 3))  # Output: 2