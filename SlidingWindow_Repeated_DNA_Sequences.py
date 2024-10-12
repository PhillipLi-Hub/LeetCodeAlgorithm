# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:32:32 2024
@author: Zhanghao

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


"""

class Solution:
    def findRepeatedDnaSequences(self,s:str) -> list[str]:
        m = dict()
        for i in range(len(s)):
            m[s[i:i+10]] = m.get(s[i:i+10],0)+1
        return [key for key,value in m.items() if value>1]

# Test samples

object_sample = Solution()
a = object_sample.findRepeatedDnaSequences(s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
print(a)