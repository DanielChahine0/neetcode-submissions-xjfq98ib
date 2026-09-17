class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = dict()
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            counter[s[r]] = counter.get(s[r], 0) + 1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l+=1
            longest = max(longest, r-l+1)
            r+=1
        return longest
            