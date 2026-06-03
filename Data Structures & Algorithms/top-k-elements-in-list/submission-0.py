class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        traverse through nums and keep a count of numbers in a dict
        output a list for all keys in dict with values >= k
        '''
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        output = []
        for i in range(k):
            output.append(sorted_items[i][0])
        return output