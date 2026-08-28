class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_checker = set()

        for num in nums:

            nums_checker.add(num)

        if len(nums) != len(nums_checker):
            return True

        return False