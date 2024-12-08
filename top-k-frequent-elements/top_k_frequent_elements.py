class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_map = {}
        freq_arr = [[] for _ in range(len(nums) + 1)]

        # nums: [1,1,1,2,2,3]
        # count_map: {1: 3, 2: 2, 3: 1}
        # freq_arr: [[], [3], [2], [1], [], [], []]

        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1

        for n, c in count_map.items():
            freq_arr[c].append(n)

        res = []
        for i in range(len(freq_arr) - 1, 0, -1 ):
            for n in freq_arr[i]:
                res.append(n)
                if len(res) == k:
                    return res

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))
