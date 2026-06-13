class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            c = ''.join(sorted(word))
            if c in seen:
                seen[c].append(word)
            else:
                seen[c] = [word]
        return list(seen.values())