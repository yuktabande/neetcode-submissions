class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        i = 0
        while i < len(nums):
            if target - nums[i] in dict:
                return [dict[target-nums[i]],i]
            if nums[i] not in dict:
                dict[nums[i]] = i
            i += 1
