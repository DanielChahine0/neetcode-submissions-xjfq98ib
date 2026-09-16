class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False

        def Counting(s):
            counter = dict()

            for c in s:
                counter[c] = counter.get(c, 0) + 1
            print(counter)
            return counter
        countS = Counting(s)
        countT = Counting(t)
        return countS==countT
