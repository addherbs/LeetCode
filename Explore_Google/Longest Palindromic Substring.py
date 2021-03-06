"""
Longest Palindromic Substring

Solution
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""

# Dynamic programming O(N**2) time approach and O(N**2) space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Setting Diagonal bits 1
        for i in range(n):  dp[i][i] = 1
        ans = [1, s[i]]
        
        # Checking palindrome for 2 pairs
        for i in range(n-1):
            if s[i] == s[i+1]: 
                dp[i][i+1] = 1
                ans = [2, s[i:i+2]]    
        
        # Checking palindrome for range greater than 2
        for i in range(2, n):
            for j in range(n-i):
                if s[j] == s[j+i] and dp[j+1][j+i-1]:
                    dp[j][j+i] = 1
                    ans = [i+1, s[j:j+i+1]]
        
        return ans[1]
        
        
        
# Expand Around Center approach O(N**2) time approach and O(N**2) space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        
        n = len(s)
        ans = [1, s[0]]
        
        for i in range(n):
            odd = self.expandAroundCenter(s, n, i, i)
            even = self.expandAroundCenter(s, n, i, i + 1)
            max_val = max(even, odd)
            if ans[0] < max_val:
                ans = [max_val, s[i-(max_val-1)//2:i+max_val//2 + 1]]
                
        return ans[1]
    
    
    def expandAroundCenter(self, s, n, left, right):
        ans = 0
        
        while left > -1 and right < n:
            if s[left] == s[right]:
                ans = right - left + 1
                left -= 1
                right += 1
            else: break
                
        return ans