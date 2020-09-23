import random
'''The goal here is to recreate as many data structures as possible with the least amount of libraries'''

def initialize_matrix():
    ''' How to initialize a zero matrix '''
    matrix = [[0 for column in range(5)] for row in range(2)]
    print(matrix)

def stack_implementation():
    '''
    Python Stack, only using lists
    '''
    print('-' * 25 + "Stack Implementation" + '-' * 25)
    stack = []
    for i in range(11):
        random_int = random.randint(1, 1000)
        print(f'{random_int} pushed to stack')
        stack.append(random_int)
    print("-" * 25 + "Switch" + "-" * 25)
    while len(stack) > 0:
        print(f'{stack.pop()} popped from stack')
    print('-' * 25 + "Stack Implementation" + '-' * 25)

def queue_implementation():
    '''
    Python Queue
    '''
    queue = []
    # While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
    print('-' * 25 + "Queue Implementation" + '-' * 25)
    for i in range(11):
        print(f'{i} pushed to stack')
        queue.append(random.randint(1,1000))
    print("-" * 25 + "Switch" + "-" * 25)
    while len(queue) > 0:
        top_element = queue.pop(0)  # Use .pop(0) to pop the front element!
        # top_element = queue[0]
        # queue = [ x for x in queue[1:]]
        print(f'{top_element} popped from stack')
    print('-' * 25 + "Stack Implementation" + '-' * 25)

    print('-' * 25 + "Stack Implementation w/ deque library" + '-' * 25)
    # The fastest way to implement a queue in python is to use a library :-/
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    queue.appendleft("LEFTY")
    queue.append("RIGHTY")
    for i in queue:
        print(i)
    print("-" * 25 + "Switch" + "-" * 25)
    while len(queue) > 0:
        print(f'{queue.popleft()} popped')
    print('-' * 25 + "Stack Implementation w/ deque library" + '-' * 25)


class ListNode:
    def __init__(self, val=None):
        self.next = None
        self.val = val


# Create a random list of linked things
def singly_linked_list():
    '''
    Python Singly Linked List
    '''
    headNode = ListNode()
    list_ptr = headNode

    list_length = random.randint(1,1000)
    print(f'Creating list of length {list_length}')
    list_items = []
    for i in range(list_length):
        rand_val = random.randint(1, 10)
        list_items.append(rand_val)
        # print (f'Adding random value {rand_val}')
        # Create a new node for each value
        newNode = ListNode(rand_val)
        list_ptr.next = newNode
        list_ptr = list_ptr.next

    # Now traverse the list
    list_ptr = headNode.next
    traversed_items = []
    while list_ptr is not None:
        # print(f'{list_ptr.val} traversed')
        traversed_items.append(list_ptr.val)
        list_ptr = list_ptr.next

    # For comparing two lists in order we can just use
    if list_items == traversed_items: print("Lists Match!")




    # Two check two lists WITHOUT ORDER we can do this a couple ways

    #If the elements are also unique, you can also convert to sets (same asymptotic runtime, may be a little bit faster in practice):
    #  set(x) == set(y)

    # Check the multisets for equality, this requires that the elements be hashable
    # You can simply check whether the multisets with the elements of x and y are equal:
    # import collections
    # collections.Counter(x) == collections.Counter(y)\
    # Both of these should be O(n)

    # Even slower we can sort both an compare them
    # If the elements are not hashable, but sortable, another alternative (runtime in O(n log n)) is
    # sorted(x) == sorted(y)



singly_linked_list()




# '''
# Python Doubly Linked List
# '''
# # In this class example each node represents a dictionary entry (key:value pair)
# # Note that you can inherit from other classes using class DoublyLinkedListNode(className):
# class DoublyLinkedListNode:
#     def __init__(self):
#         self.key = None
#         self.value = None
#         self.prev = None
#         self.next = None



initialize_matrix()
stack_implementation()
queue_implementation()