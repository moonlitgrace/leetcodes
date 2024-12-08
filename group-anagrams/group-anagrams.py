class Solution:
    def groupAnagrams(self, strs):
        anagrams_map = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if not sorted_s in anagrams_map:
                anagrams_map[sorted_s] = [s]
            else:
                anagrams_map[sorted_s].append(s)

        return list(anagrams_map.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
