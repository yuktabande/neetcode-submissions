class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        maintain a pointer on each number, and a list of before and after of that elements
        after will contain entire array except 1st and before will be empty 
        1st ele -> product of after 
        2nd ele -> append 1st ele to before, remove from after
        multiply before and after
        '''
        result = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if i!=j:
                    product *= nums[j]
            result.append(product)
        return result

