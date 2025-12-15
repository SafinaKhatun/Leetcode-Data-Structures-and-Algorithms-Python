 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {} 

        # 'enumerate' gives us both the index (i) and the value (num) at the same time.
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen_numbers:
                return [seen_numbers[complement], i]
        
            seen_numbers[num] = i
        
        return []
        