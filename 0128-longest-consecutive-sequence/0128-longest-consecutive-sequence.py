class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = defaultdict(list)
        res = 0
        uniqueNums = set(nums)

        for num in uniqueNums:
            if num - 1 in uniqueNums:
                continue
            else: 
                seq[num].append(num)
                curr = num + 1
                while curr in uniqueNums:
                    seq[num].append(curr)
                    curr += 1
                res = max(res, len(seq[num]))

        return res