class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping tuple letter count of words to list of anagrams

        for word in strs:
            counter = [0] * 26 # counting letters

            for ch in word:
                counter[ord(ch) - ord('a')] += 1 # ord() to find ascii of character
            
            res[tuple(counter)].append(word) # dictionary cannot have mutable keys - list, so we used immutable keys - tuples

        return list(res.values())