from typing import List

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        # Initialize the result variable 'ans' to store the final sum of power
        # 't' is a temporary variable to accumulate the sum of powers
        # 'base' is used to perform modulo 10^9 + 7 to prevent integer overflow
        ans, t, base = 0, 0, 10**9 + 7
        
        # Iterate over the sorted 'nums' list (sorting ensures elements are processed in ascending order)
        for c in sorted(nums):
            # Update 'ans' by adding the current power contribution for this element 'c'
            ans = (ans + (t + c) * c * c) % base
            
            # Update 't' which is used in the next iteration
            # 't' keeps track of the accumulated sum from previous iterations
            t = (2 * t + c) % base
        
        # Return the final sum of powers modulo 10^9 + 7
        return ans
