# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:41:52 2024

@author: 11722

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

class Solution:
    def minSubArrayLen(self,target:int,nums:list[int]) ->int:
        w_sum = 0
        ans = float('inf')
        start = 0
        for i in range(len(nums)):
            w_sum+=nums[i]
            while w_sum>=target:
                ans = min(ans,i-start+1)
                w_sum-=nums[start]
                start+=1
        return 0 if ans == float('inf') else ans
    
object_test = Solution()
test_result = object_test.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])