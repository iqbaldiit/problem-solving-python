'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times). Given two strings str1 and str2, 
return the largest string x such that x divides both str1 and str2. 
Example 1: Input: str1 = "ABCABC", str2 = "ABC" Output: "ABC" 
Example 2: Input: str1 = "ABABAB", str2 = "ABAB" Output: "AB" 
Example 3: Input: str1 = "LEET", str2 = "CODE" Output: "" 

Constraints: 1 <= str1.length, str2.length <= 1000 str1 and str2 consist of English uppercase letters.
'''

def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:gcd(len(str1), len(str2))]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
print(gcd_of_strings("ABCABC", "ABC"))   # Output: "ABC"
print(gcd_of_strings("ABABAB", "ABAB"))  # Output: "AB"
print(gcd_of_strings("LEET", "CODE"))    # Output: ""
