class PrefixNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    

class PrefixTree:

    def __init__(self):
        self.tree = PrefixNode()

    def insert(self, word: str) -> None:
        node = self.tree
        for ch in word:
            if ch not in node.children:
                node.children[ch] = PrefixNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.tree
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.tree
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
        