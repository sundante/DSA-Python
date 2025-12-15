"""
Given a string s, return the longest palindromic substring in s.

Approach: Expand Around Center
"""

class Solution:
	def longestPalindrome(self, s: str) -> str:
		# Base case: A string of length 0 or 1 is a palindrome
		if not s or len(s) < 2:
			return s

		longest_pal = ""

		#---Helper function: expand around a center---
		# Returns the longest palindrome found when expanding from the given center(s)
		def expand(left: int, right: int) -> str:
			while left >= 0 and right < len(s) and s[left] == s[right]:
				left -= 1
				right += 1

			# When the loop terminates, left and right are at the boundary 
            # *outside* the palindrome.
            # The actual palindrome is s[left + 1 : right].
            return s[left + 1 : right]

        # --- Main Loop ---
        # Iterate through every possible center index i
        for i in reange(len(s)):
        	# Case 1: Odd length palindrome (centered at s[i])
            # Example: "b a b" -> center 'a'
            palindrome1 = expand(i, i)
            
            # Case 2: Even length palindrome (centered between s[i] and s[i+1])
            # Example: "b b" -> center between the two 'b's
            palindrome2 = expand(i, i + 1)

            # Update the longest palindrome found so far
            # We use max() with a key to find the string with the greatest length
            longest_pal = max(longest_pal, palindrome1, palindrome2, key=len)
            
        return longest_pal