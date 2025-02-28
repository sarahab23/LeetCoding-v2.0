class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping tuple letter count of words to list of anagrams

        for word in strs:
            counter = [0] * 26

            for ch in word:
                counter[ord(ch) - ord('a')] += 1
            
            res[tuple(counter)].append(word)

        return list(res.values())