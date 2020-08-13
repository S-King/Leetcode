
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''


class Solution:
    # def expand_odd(self, s: str, left: int, right: int) -> str:
    # def expand_even(self, s: str, left: int, right: int) -> str:

    # At every possible location consider if it could be the center of an even or odd palindrome
    # So there are possibly 2n-1 centers (since they can be between numbers
    # and at each center it could take up to n time to compare => O(n^2) time but constant space => O(1)
    def expand(self, s: str, l_ptr: int, r_ptr : int) -> str:
        len_s = len(s)

        # While we are still in bound continue to expand, notice that the left bound it >= since our final range
        # is inclusive on the lower side (once we get to below zero or equal to len we have gone out of bounds)
        while (l_ptr >= 0 and r_ptr < len_s and s[l_ptr] == s[r_ptr]):
            l_ptr -= 1
            r_ptr += 1
        return s[l_ptr + 1: r_ptr]


    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest_palindrome = ""
        longest_palindrome_len = 0

        for i in range(len(s) - 1):

            even_palindrome = self.expand(s, i, i)
            odd_palindrome = self.expand(s, i, i + 1)

            if len(even_palindrome) > longest_palindrome_len:
                longest_palindrome = even_palindrome
                longest_palindrome_len = len(even_palindrome)
            # MESSED UP HERE WITH AN ELIF but in reality needed to be able to consider both the even and the odd palindrome being
            # larger than the current max, they are unrelated, BE CAREFUL!
            if len(odd_palindrome) > longest_palindrome_len:
                longest_palindrome = odd_palindrome
                longest_palindrome_len = len(odd_palindrome)
        return longest_palindrome



    # Alright lets give this dynamic programming a shot
    def longestPalindrome_dynamicProgramming(self, s: str) -> str:
        # First we need to consider all possible substrings, n^2 combinations
        len_s = len(s)
        answer_coordinates = [0,0]

        # Since all letters are single char palindromes just initialize the first letter as the longest palindrome
        if len_s == 0:
            # Always ask what return types are expected for edge cases like empty strings
            # return None
            return ""

        # WARNING, DONT USE THIS TO CREATE 2D array!! It causes [1][1] to refer to all the first elements
        # dp_array = [[0] * len_s] * len_s
        dp_array = [ [0] * len_s for x in range(len_s)]

        # Next initialize the base cases
        # All single letters are palindromes
        for i in range(len_s):
            dp_array[i][i] = 1
            # Don't forget to set these as the possible longest palindromes
            answer_coordinates = [i,i]

        # Fill in the table with any two letter palindrome centers
        for i in range(len_s - 1):
            if s[i] == s[i+1]:
                dp_array[i][i+1] = 1
                answer_coordinates = [i, i+1]

        # Now we need to check all palindromes three letters long and larger
        '''   Now we have filled in the table, first with caps, then with the doubles in lowercase, must fill in the final values
                +---+---+---+---+---+---+---+---+
                |   |   | x | a | b | a | a | y |
                |   |   | 0 | 1 | 2 | 3 | 4 | 5 |
                +---+---+---+---+---+---+---+---+
                | x | 0 | T | f |   |   |   |   |
                | a | 1 | F | T | f |   |   |   |
                | b | 2 | F | F | T | f |   |   |
                | a | 3 | F | F | F | T | t |   |
                | a | 4 | F | F | F | F | T | f |
                | y | 5 | F | F | F | F | F | T |
                +---+---+---+---+---+---+---+---+
        '''

        # Here is a good example of how to fill this table in when the values are all shifted like above
        shift = 2
        for shift_value in range(shift, len(s), 1):
            for y in range(0, len(s) - shift_value, 1):
                x = y + shift_value
                print("x:{}, y:{}".format(x, y))
                if s[x] == s[y] and dp_array[y+1][x-1] == 1:
                    dp_array[y][x] = 1
                    answer_coordinates = [y,x]

        # Don't forget that this (python's) range isn't inclusive but our algorithm's range is!!
        return s[answer_coordinates[0] : answer_coordinates[1] + 1]







# q = 'cbbdbbx'
q = 'cbbd'
mySolution = Solution()
# ans = mySolution.longestPalindrome(q)
# print(ans)

ans = mySolution.longestPalindrome_dynamicProgramming(q)
print(ans)