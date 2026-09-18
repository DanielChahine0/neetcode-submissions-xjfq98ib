class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0; r = 0
        maxV = 0
        

        while r < len(s):
            subLen = r - l + 1
            counter[s[r]] = counter.get(s[r], 0) + 1
            mostFrequent = max(counter.values())
            # print(counter)
            while subLen-mostFrequent > k:
                # print(counter)
                counter[s[l]]-=1
                subLen -=1
                l+=1
            # print(mostFrequent)

            maxV = max(maxV, subLen)
            r+=1
        
        return maxV