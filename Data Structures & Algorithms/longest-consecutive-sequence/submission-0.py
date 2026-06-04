class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        maintain a seen dict
        and to track length max_len, temp_len
        for each element, it will check if a smaller ele with smaller pos exists
        if it does it will add to the length 
        '''
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
