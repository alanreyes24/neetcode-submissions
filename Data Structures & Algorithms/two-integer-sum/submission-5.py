class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):

            compliment = target - nums[i]

            if compliment in seen:

                if i != seen[compliment]:
                    return[min(i, seen[compliment]), max(i, seen[compliment])]

            seen[nums[i]] = i