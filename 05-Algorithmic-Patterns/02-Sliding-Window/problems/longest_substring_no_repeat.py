class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # A set to store characters in the current window (for O(1) average lookup time)
        char_set = set()
        
        # Left pointer of the sliding window
        L = 0
        
        # Variable to store the maximum length found so far
        max_length = 0
        
        # Right pointer of the sliding window
        # We iterate through the string using the right pointer R
        for R in range(len(s)):
            
            # --- Contract the Window (Handle Duplicates) ---
            # If the character at R is already in the set, it's a duplicate.
            # We contract the window by moving L forward until the duplicate is gone.
            while s[R] in char_set:
                # Remove the character at the left pointer L
                char_set.remove(s[L])
                # Move the left pointer L to the right
                L += 1
                
            # --- Expand the Window ---
            # The character at R is now unique within the window s[L..R]
            char_set.add(s[R])
            
            # --- Update Result ---
            # The current window length is R - L + 1
            max_length = max(max_length, R - L + 1)
            
        return max_length