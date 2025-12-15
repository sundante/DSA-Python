"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # 1. Sort the array
        nums.sort()
        result = []
        N = len(nums)
        
        # 
        
        # Iterate through the array to fix the first number (nums[i])
        for i in range(N):
            
            # Optimization: If the current number is greater than 0, 
            # since the array is sorted, the sum of three numbers cannot be 0.
            if nums[i] > 0:
                break
                
            # Skip duplicates for the fixed number (i)
            # We check i > 0 to ensure we don't skip the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Set up the Two Pointers for the remaining part of the array
            j = i + 1  # Left pointer
            k = N - 1  # Right pointer
            
            # The required sum for the two pointers is the negative of the fixed number
            target = -nums[i]
            
            # 2. Two Pointers (Converging)
            while j < k:
                current_sum = nums[j] + nums[k]
                
                if current_sum == target:
                    # Found a triplet
                    result.append([nums[i], nums[j], nums[k]])
                    
                    # Skip duplicates for the second number (j)
                    # Must be done *after* finding a valid triplet
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    
                    # Skip duplicates for the third number (k)
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    # Move both pointers to continue the search
                    j += 1
                    k -= 1
                    
                elif current_sum < target:
                    # Sum is too small, need a larger number, move the left pointer (j)
                    j += 1
                else: # current_sum > target
                    # Sum is too large, need a smaller number, move the right pointer (k)
                    k -= 1
                    
        return result