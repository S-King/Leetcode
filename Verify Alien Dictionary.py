from typing import List
'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order
of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
given words are sorted lexicographicaly in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to
lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less
than any other character (More info).

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.
'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # Make a hash table to lookup the order
        order_hashtable = {letter: index for index, letter in enumerate(order)}

        # xrange is really fast apparently so use it where you can
        # range is inclusive but we don't want to use the last position since we are comparing to the
        # next word in every step
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


mySolution = Solution()
mySolution.isAlienSorted()

