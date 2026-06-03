class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        traverse through each word and sort it  
        add it to seen dict with sorted word:real word
        then from the seen, all words with same dict need to str
        str gets appended to output. 
        '''

        seen = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in seen:
                seen[key] = []
            seen[key].append(word)
        return list(seen.values())