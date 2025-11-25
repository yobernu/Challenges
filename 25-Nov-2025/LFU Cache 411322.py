# Problem: LFU Cache - https://leetcode.com/problems/lfu-cache/


class Node:
    def __init__(self, key, val, freq=1, next=None, prev=None):
        self.key, self.val, self.freq = key, val, freq
        self.next, self.prev = next, prev

class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0 # length of list 

    def addAtHead(self, node):
        # add a node right after head (MRU)
        nxt = self.head.next 
        self.head.next, node.next = node, nxt 
        nxt.prev, node.prev = node, self.head
        self.size += 1

    def removeNode(self, node):
        # remove node from a list 
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1

    def removeFromTail(self):
        # remove and return the node right before tail (LRU node)
        if self.size == 0:
            return None 
        lru = self.tail.prev
        self.removeNode(lru)
        return lru 

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity # capacity of cache
        self.cache = {} # key --> node
        self.freq_map = defaultdict(DoublyLinkedList) # frequency --> list
        self.min_freq = 0 

    def _update_freq(self, node):
        # handles frequency and recency; performs Frequency Hop operation in O(1)
        # removes from old list -> update min_freq (if necessary) --> increament frequency --> Add to new list (MRU position)
        freq = node.freq
        self.freq_map[freq].removeNode(node)
        # if this was min_freq and the min_freq list is now empty, then update min_freq (increment it)
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
        # increment frequency and add to new list 
        node.freq += 1
        self.freq_map[node.freq].addAtHead(node)

    def get(self, key):
        if key not in self.cache:
            return -1 
        node = self.cache[key]
        self._update_freq(node)
        return node.val 

    def put(self, key, value):
        # add a node (key, val) to the cache 
        if self.capacity == 0:
            return 
        if key in self.cache:
            # update the value 
            node = self.cache[key]
            node.val = value
            self._update_freq(node)
        else:
            # check if we have capacity or not 
            if len(self.cache) >= self.capacity:
                # evict lfu and lru among lfue 
                lfu_list = self.freq_map[self.min_freq]
                evict_node = lfu_list.removeFromTail()
                del self.cache[evict_node.key]
            # insert new node 
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.freq_map[1].addAtHead(new_node)
            self.min_freq = 1




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)