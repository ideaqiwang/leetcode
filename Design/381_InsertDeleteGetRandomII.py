'''
381. Insert Delte GetRandon O(1) - Duplicates Allowed

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item was present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements (it's guaranteed that at least one element exists when this method is called). The probability of each element being returned is linearly related to the number of same values the multiset contains.
'''

from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array_ = []
        self.value2index_ = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.value2index_[val].add(len(self.array_))
        self.array_.append(val)
        return len(self.value2index_[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.value2index_[val]:
            return False
        removeIdx, last = self.value2index_[val].pop(), self.array_[-1]
        self.array_[removeIdx] = last
        self.value2index_[last].add(removeIdx)
        self.value2index_[last].discard(len(self.array_)-1)
        self.array_.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.array_)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()