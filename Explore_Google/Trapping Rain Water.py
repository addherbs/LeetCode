"""
Trapping Rain Water

Solution
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        n = len(height)
        ans = 0
        
        left = [0] * n
        left[0] = height[0]
        
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        r_max = height[-1]
        for i in range(n-1, -1, -1):
            r_max = max(r_max, height[i])
            ans += min(left[i], r_max) - height[i]
        
        return ans