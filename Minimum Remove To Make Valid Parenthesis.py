
# State the answer in words
# Use a stack, for every opening paranthesis push a value onto the stack and for

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # Keep a count of forward and backward parenthesis
        opening_parenthesis_behind = 0
        closing_parenthesis_ahead = 0

        s_list = list(s)
        letters_indices_to_remove = []

        for letter in s_list:
            if letter == ")": closing_parenthesis_ahead += 1

        for i, letter in enumerate(s_list):

            if letter == ")" and opening_parenthesis_behind == 0:
                letters_indices_to_remove.append(i)
            elif letter == ")" and opening_parenthesis_behind > 0:
                closing_parenthesis_ahead -= 1

            elif letter == "(" and closing_parenthesis_ahead == 0:
                letters_indices_to_remove.append(i)
            elif letter == "(" and closing_parenthesis_ahead > 0:
                opening_parenthesis_behind += 1

        for i in letters_indices_to_remove[::-1]:

            s_list.pop(i)


        return "".join(s_list)


    def minRemovalToMakeValid_Stack(self, s:str) -> str:
        paran_stack = []
        letters_to_remove = []

        s_list = list(s)
        for i, letter in enumerate(s_list):
            # If we find a closing parenthesis then see if we have an opening parenthesis on the stack
            if letter == ")":
                if paran_stack:
                    paran_stack.pop()
                else:
                    letters_to_remove.append(i)
            elif letter == "(":
                paran_stack.append(i)

        letters_to_remove += paran_stack
        final_result = []
        for i, letter in enumerate(s_list):
            if i not in letters_to_remove:
                final_result.append(letter)

        return "".join(final_result)






s= "lee(t(c)o)de)"
mySolution = Solution()
result = mySolution.minRemovalToMakeValid_Stack(s)
print(result)




# If i get to a closing parenthesis I need to know if there is an opening parenthesis BEHIND ME I can use, if there isn't I need to pop it
# If I get to an opening parenthesis I need to know if there is a closing parenthesis IN FRONT OF ME left to close it

# Variables:
# opening_parenthesis_behind = 0
# closing_parenthesis_ahead = 0

