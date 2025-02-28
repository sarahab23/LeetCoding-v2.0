class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        ans = []
        prevWords = {}

        for word in strs:
            sortedW = ''.join(sorted(word))
            if sortedW in prevWords:
                ans[prevWords[sortedW]].append(word)
            else:
                ans.append([word])
                prevWords[sortedW] = count
                count = count + 1
        
        return ans