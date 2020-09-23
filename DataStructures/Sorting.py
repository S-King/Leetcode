from typing import List
import random


words = ["word", "world", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"
# Make a hash table to lookup the order
order_hashtable = {letter: index for index, letter in enumerate(order)}

# O(N * M), where N is len(words), M is average length of each word. -- TIME
# O(1) -- SPACE
def check_list_of_strings_is_sorted(words: list, order: str) -> bool:
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        # An important thing to realize is that you only need to look for the first difference,
        # that is the point where you can determine sorted-ness and stop
        for letter_position in range(min(len(word1), len(word2))):
            if word1[letter_position] != word2[letter_position]:
                if order_hashtable[word1[letter_position]] > order_hashtable[word2[letter_position]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False
    return True


strings = ["word 3", "world 1", "world 0 ", "row abc"]
def sort_list_of_strings_regularOrder(strings: list) -> list:
    # Here is an example of sorting on the second value first then the first value, we will also prioritize alphas
    def sort_function(list_item):
        # string.split(separator, maxsplit) # Maxsplit = Specifies how many splits to do. Default value is -1, which is "all occurrences"
        # Split on spaces but only do it on the first space occurrence
        first_item, rest_of_list = list_item.split(" ", 1)

        # Return a tuple of the things we will use to sort
        if rest_of_list.isalpha():
            sorting_tuple = (0, )
        else:
            sorting_tuple = (1, rest_of_list, first_item)
        return sorting_tuple

    sorted_list = sorted(strings, key = sort_function)
    return sorted_list

print ("-" * 25 + "Sort Strings - Alphabetic + Constraints" + "-" * 25)
print("Initial strings: {}".format(str(strings)))
sorted_strings = sort_list_of_strings_regularOrder(strings)
print("Sorted strings: {}".format(str(sorted_strings )))



def sort_list_of_strings_arbitraryOrder(strings: list, order: str) -> list:
    # associate each char with the index in the string
    # this makes sort faster for multiple invocations when compared with
    # ORDER.index(c)

    POS = {c: p for (p, c) in enumerate(order)}

    strings.sort(key=lambda c: POS[c])
    # or, suggested by wim
    strings.sort(key=POS.get)

class MyStrOrder:
    def __init__(self, inner):
        self.inner = inner

    def __lt__(self, other):
        order = "worldabcefghijkmnpqstuvxyz"
        POS = {c: p for (p, c) in enumerate(order)}
        for i in range(min(len(self.inner), len(other.inner))):
            a = POS.get(self.inner[i])
            b = POS.get(other.inner[i])
            if a != b:
                return a < b
        return len(self.inner) < len(other.inner)

print ("-" * 25 + "Sort Strings - Arbitrary Order" + "-" * 25)
lst = ["abc", "ab", "a"]
print(lst)
lst.sort(key = MyStrOrder)
print(lst)


# Merge sort from scratch

# Need to keep splitting the array into
def mergeSort_ListOfNumbers(int_list : List[int]) -> List[int]:
    # DONT NEED! We can just use the input array
    # sorted_list = []

    # While we have more than one element keep splitting the array
    if len(int_list) > 1:

        middle = len(int_list) // 2 # Do a floor division but Pythons upper bound on ranges in exclusive anyway
        left = int_list[:middle]
        right = int_list[middle:]

        # This recursive call will continue to split the lists until there are less than 2 in each list
        mergeSort_ListOfNumbers(left)
        mergeSort_ListOfNumbers(right)

        # Then we can begin combining them from the bottom up
        i = 0 # Counter for left side
        j = 0 # Counter for right side
        k = 0 # Counter for final sorted list

        while i != len(left) and j != len(right):
            if left[i] < right[j]:
                int_list[k] = left[i]
                k += 1
                i += 1
            else:
                int_list[k] = right[j]
                k += 1
                j += 1

        # Now there still could be some unconsumed elements remaining the we need to add
        # Add anything remaining on the left side
        for remainder in range(i,len(left), 1):
            int_list[k] = left[remainder]
            k += 1

        for remainder in range(j,len(right), 1):
            int_list[k] = right[remainder]
            k += 1

        return int_list

# Merge sort is stable, meaning that equal items preserve their order
# when dividing by two we will have log(n) steps or merges in this case
# then we need to combine the original n elements in n time => O(n log(n))
print ("-" * 25 + "MERGE SORT O(N log" + "-" * 25)
unsorted_list = [random.randrange(-99, 99) for x in range(10)]
print ("Unsorted Numbers {}".format(unsorted_list))
sorted_list = mergeSort_ListOfNumbers(unsorted_list)
print ("Sorted Numbers {}".format(sorted_list))