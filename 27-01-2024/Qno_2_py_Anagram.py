'''Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

Example

Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

Function Description

Complete the anagram function in the editor below.

anagram has the following parameter(s):

string s: a string
Returns

int: the minimum number of characters to change or -1.
Input Format

The first line will contain an integer, , the number of test cases.
Each test case will contain a string .

Constraints


 consists only of characters in the range ascii[a-z].
Sample Input

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx
Sample Output

3
1
-1
2
0
1'''

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Check if the length of the string is even
    if len(s) % 2 != 0:
        return -1

    # Split the string into two substrings
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    # Count the frequency of characters in each substring
    count_s1 = [0] * 26
    count_s2 = [0] * 26

    for char in s1:
        count_s1[ord(char) - ord('a')] += 1

    for char in s2:
        count_s2[ord(char) - ord('a')] += 1

    # Calculate the minimum number of changes needed
    changes = 0
    for i in range(26):
        changes += abs(count_s1[i] - count_s2[i])

    # Return the result
    return changes // 2

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for _ in range(q):
        s = input().strip()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close(
