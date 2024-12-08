var topKFrequent = function(nums, k) {
  const count_map = {}
  const freq_arr = Array.from({ length: nums.length + 1 }, () => [])

  for (const n of nums) {
    count_map[n] = (count_map[n] || 0) + 1
  }

  for (const [n, c] of Object.entries(count_map)) {
    freq_arr[c].push(parseInt(n)) 
  }

  res = []
  for (let i=freq_arr.length - 1; i > 0; i--) {
    for (const n of freq_arr[i]) {
      res.push(n)
      if (res.length === k) {
        return res
      }
    }
  } 
};

console.log(topKFrequent([1,1,1,2,2,3], 2))
