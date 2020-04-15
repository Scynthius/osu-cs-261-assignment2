# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# Author: Jonathan Fryman
# Date: 4/14/2020
# ===================================================

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False
def is_balanced(input_string):
    """
    Takes as input a string (can be NULL) and determines if the parentheses within the string are balanced. Returns
    True if they are balanced or if string is Null, and False if they are not.
    """
    stack = []
    # Holds the list of characters recognized by the program.
    openers = ["(", "[", "{"]
    closers = [")", "]", "}"]
    if not input_string:
        return True
    for i in input_string:
        if i in openers:
            # Add any opening parentheses to the stack.
            stack.append(i)
        elif i in closers and stack:
            # Pop the last stack element and ensure the parentheses match.
            match = stack.pop()
            if openers.index(match) != closers.index(i):
                # Uses relative position of character lists to match pairs.
                return False
        elif i in closers and not stack:
            # The closing bracket has to mate. Unbalanced string.
            return False
    if not stack:
        # After all characters are tested, stack should be empty.
        return True
    else:
        return False


if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))