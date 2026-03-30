class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count the characters of t
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        need = len(count.keys())

        l = 0
        results = []
        have = 0
        countR = {}
        for r in range(len(s)):
            # Check if the character should be counted
            if s[r] in t:
                countR[s[r]] = countR.get(s[r], 0) + 1
                # If we match the value in both maps, update the have
                if countR[s[r]] == count[s[r]]:
                    have += 1
            
            # Consider all the valid windows
            while have == need:
                print(l, r, countR)
                results.append(s[l:r+1])
                print(s[l])
                if s[l] in count:
                    countR[s[l]] -= 1
                    if countR[s[l]] < count[s[l]]:
                        have -=1
                l+=1

        result = ""
        if len(results) != 0:
            result = results[0]

        for item in results:
            if len(item) < len(result):
                result = item

        return result