class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for item in strs:
            encodedStr += str(len(item)) +"#"+ item
        print(encodedStr)
        return encodedStr

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        items = []
        while i<n:
            j = i
            while j<n and s[j]!="#":
                j+=1
            wordLen = int(s[i:j])
            j+=1
            items.append(s[j:j+wordLen])
            i = j+wordLen
        return items