# First brainstrom from a high level, goal is O(1)
# Could use a queue or stack which is brought to the front (or back) or the structure
# whenever it is accessed


# class LRUCache:
#     def __init__(self, capacity: int):
#         # If we count 'put' as an activity then we want recently added items to also be near the top
#         # of the recently added queue. (FIFO - the first (oldest) item should be the first out)
#         # First instantiate the list to serve as our queue
#         LRU_queue = {}
#         LRU_capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key in self.LRU_queue:
#             return 1
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         # If we have room then just add it (to the front)
#         if len(LRU_queue) < self.capacity:
#             LRU_queue.insert(0, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# didn't like the approach above, we can just keep track of the last used item, we are only
# interested in that one and we can update the state when that one changes

# Create a linked list with the oldest item on the bottom
# keep track of the root node and end node, if that is touched then update the root node
# to be the root node's child and put the newly touched node at the end

# ORDERED DICTS!!!!!!

from collections import OrderedDict

# This will be an OrderedDict with the added constraint of having a capacity/limit

class LRUCache_OrderedDict(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    # This just needs to check if the key exists, and if it does we need to move it to the top of the dictionary
    # since it was most recently active/selected
    def get(self, key: int) -> int:
        if key in self:
            # Update this key to be most recently used (the front of the queue)
            self.move_to_end(key)

            return self[key]
        else:
            return -1

    # Add this value to the cache, if the cache is full remove the most recently used
    def put(self, key: int, value: int) -> None:
        # Need to account for both SET and INSERT !!!
        if key in self:
            self[key] = value
            self.move_to_end(key)
        else:
            # If we have room just add it to the front of the list
            if len(self) < self.capacity:
                self[key] = value
            # If we don't have room then pop the item from the front of the list and all this to the end
            else:
                self.popitem(last=False)
                self[key] = value


# In this class example each node represents a dictionary entry (key:value pair)
# Note that you can inherit from other classes using class DoublyLinkedListNode(className):
class DoublyLinkedListNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

# The benefit of using a static head and tail node is that we don't have to update the state for these points
# after every time the dictionary is altered
# The benefit if using a doubly linked list is that we can remove nodes without

# Single underscore just means (kind of) private method
# Double underscores allow "name mangling aka name concatenation" where __age becomes _LRUCache_DoublyLinkedHashTable__age
class LRUCache_DoublyLinkedHashTable():
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

class LRUCache():
    def __init__(self, capacity: int):
        # Create the head and tail nodes for out doubly linked list
        self.headNode, self.tailNode = DoublyLinkedListNode(), DoublyLinkedListNode()
        # When working with a linked list where size matters make sure to keep track of the size of the dictionary
        # to prevent having to traverse the entire list when the length is needed
        self.length = 0
        self.capacity = capacity
        # This will be a queue in the form of key:node
        self.queue = {}

        self.headNode.next = self.tailNode
        self.tailNode.prev = self.headNode

    def _move_to_end(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _remove_node(self, node):
        # When removing an item from a linked list its 3 steps
        # 1 - Retrieve the node we need
        node_to_remove = node
        # 2 - Link the previous to the next
        node_to_remove.prev.next = node_to_remove.next
        # 3 - Link the next to the previous
        node_to_remove.next.prev = node_to_remove.prev
        self.length -= 1

    # We will add the node to the end
    def _add_node(self, node):
        # Attach the node between the two nodes we want
        node_to_add = node
        node_to_add.next = self.tailNode
        node_to_add.prev = self.tailNode.prev

        # Update the connections between the two nodes to point at the new node
        # MAKE SURE TO UPDATE THE PREVIOUS NODE ATTRIBUTES BEFORE UPDATING PREV NODE REFERENCE!!!
        self.tailNode.prev.next = node_to_add
        self.tailNode.prev = node_to_add
        self.length += 1

    # Get returns value if key exists or -1 otherwise
    def get(self, key: int) -> int:
        if self.queue.get(key) is not None:
            lookup_node = self.queue[key]
            # Move this key to the (right) end of the doubly linked list
            self._move_to_end(lookup_node)
            return lookup_node.value
        else:
            return -1

    # Set or insert the value if the key is not already present. When the cache reached its capacity,
    # it should invalidate the least recently used item before inserting a new item.
    def put(self, key: int, value: int) -> None:
        if self.queue.get(key) is not None:
            lookup_node = self.queue[key]
            lookup_node.value = value
            self._move_to_end(lookup_node)
            return None

        new_node = DoublyLinkedListNode()
        new_node.key, new_node.value = key, value
        self.queue[key] = new_node
        if self.length < self.capacity:
            # Create a new node, add it to the end of the linked list, then add it the cache
            self._add_node(new_node)
        else:
            # Remove a node from the head and add the new node to the beginning
            # References can you kill with confusion!! Just grab a copy of the variables you'll need before messing with the linked list
            key_to_remove = self.headNode.next.key
            self._remove_node(self.headNode.next)
            del self.queue[key_to_remove]
            self._add_node(new_node)
        return None

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)

answer = obj.get(2)  #null
answer = obj.put(1,1)#null
answer = obj.put(2,2)#null
answer = obj.get(1)  #1
answer = obj.put(3,3)#null
answer = obj.get(2)  #-1
answer = obj.put(4,4)#null
answer = obj.get(1)  #-1
answer = obj.get(3)  #3
answer = obj.get(4)  #4
