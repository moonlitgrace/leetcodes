var groupAnagrams = function (strs) {
  const anagramsMap = {}

  for (const s of strs) {
    const sorted_s = s.split('').sort().join('')
    if (anagramsMap[sorted_s]) {
      anagramsMap[sorted_s].push(s)
    } else {
      anagramsMap[sorted_s] = [s]
    }
  }

  return Object.values(anagramsMap)
}

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
