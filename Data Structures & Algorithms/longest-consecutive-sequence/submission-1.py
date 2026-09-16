class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest=0
        
        for n in numSet:
            # if n is the start
            if n-1 not in numSet:
                # check till what number it reaches
                length = 1
                while n+length in numSet:
                    length+=1
                longest = max(longest, length)

        return longest
