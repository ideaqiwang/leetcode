'''
380. Insert Delete GetRandon O(1)

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
'''

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value2index_ = {}
        self.array_ = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.value2index_:
            return False
        self.value2index_[val] = len(self.array_)
        self.array_.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.value2index_:
            return False
        lastElement, idx = self.array_[-1], self.value2index_[val]
        self.array_[idx], self.value2index_[lastElement] = lastElement, idx
        self.array_.pop()
        del self.value2index_[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.array_)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()