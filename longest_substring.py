# Brute Force (O(n^2)) Solution Below:
def get_nonrepeating_substrings(s: str) -> list[str]:
    substrings = []
    for i in range(len(s)):
       chars = {}
       for j in range(i, len(s)):
           if s[j] in chars:
               break
           else:
               substrings.append(s[i:j+1])
               chars[s[j]] = True

    return substrings

def longest_substring(s: str) -> int:
    substrings = get_nonrepeating_substrings(s)
    max = 0
    for substring in substrings:
        if len(substring) > max:
            max = len(substring)

    return max

# O(n) Solution Below:
def lengthOfLongestSubstring(s: str) -> int:

# initialize max_length. to compare and start pointer to traverse
    max_length = start = 0

# initializing a dictionary to keep track of positions already traversed
    used = {}

# Loop for idx position and c is character in the string s
    for idx, c in enumerate(s):
        # Check if c is used. If used then set the start pointer to the
        # position where this charcter was last observed + 1. 
        # The +1 is to ensure to start and lookout for the new substring. 
        if c in used and used[c] >= start:
            start = used[c] + 1

        else:
            max_length = max(max_length, idx-start+1)

        used[c] = idx

    return max_length
