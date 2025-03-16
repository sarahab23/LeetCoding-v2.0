class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key, self.val = key, val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cap, self.cache = capacity, {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def removeNode(self, curr):
        del self.cache[curr.key] 
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        
    def addNode(self, key, value):
        prevN = self.right.prev
        dummy = Node(key, value, self.right, prevN)
        prevN.next = dummy
        self.right.prev = dummy
        self.cache[key] = dummy

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        curr = self.cache[key]
        if self.right.prev != curr:
            self.removeNode(curr)
            self.addNode(key, curr.val)
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        if len(self.cache) >= self.cap:
            self.removeNode(self.left.next)
        self.addNode(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)