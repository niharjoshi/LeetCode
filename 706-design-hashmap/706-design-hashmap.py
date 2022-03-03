class ListNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hash_table = [None] * self.size
        
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.hash_table[index] == None:
            self.hash_table[index] = ListNode(key, value)
        else:
            curr = self.hash_table[index]
            while True:
                if curr.key == key:
                    curr.val = value
                    return
                if curr.next == None:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)
                    
        
    def get(self, key: int) -> int:
        index = key % self.size
        curr = self.hash_table[index]
        while curr != None:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
        
    def remove(self, key: int) -> None:
        index = key % self.size
        curr = prev = self.hash_table[index]
        if not curr:
            return
        if curr.key == key:
            self.hash_table[index] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    break
                prev, curr = prev.next, curr.next
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)