'''
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.next = None

class LRUCache:
    # LinkedList + HashMap
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2prenode = {} # Can avoid a prev pointer
        self.dummy = Node()
        self.tail = self.dummy

    def get(self, key: int) -> int:
        if key not in self.key2prenode:
            return -1
        
        curNode = self.key2prenode[key].next
        value = curNode.value
        self.kick(curNode)
        return value
       
    def put(self, key: int, value: int) -> None:
        if key not in self.key2prenode:
            node = Node(key, value)
            self.push_back(node)
            if len(self.key2prenode) > self.capacity:
                self.pop_front()
        else:
            curNode = self.key2prenode[key].next
            curNode.value = value
            self.kick(curNode)
    
    def kick(self, node):
        if node == self.tail:
            return
        preNode = self.key2prenode[node.key]
        nextNode = node.next
        preNode.next = nextNode
        self.key2prenode[nextNode.key] = preNode
        node.next = None
        self.push_back(node)
        
    def push_back(self, node):
        self.tail.next = node
        self.key2prenode[node.key] = self.tail
        self.tail = node
        
    def pop_front(self):
        head = self.dummy.next
        newHead = head.next
        self.dummy.next = newHead
        del self.key2prenode[head.key]
        self.key2prenode[newHead.key] = self.dummy
