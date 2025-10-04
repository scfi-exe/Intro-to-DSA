# Given a string s containing just the characters "(", ")", "{". "}", "[", and "]", determine if the input string is valid
# A string is valid if:
# 1. Open brackets must be closed by the same type of brackets
# 2. Open brackets must be closed in the correct order

# s = "()" --> output == True
# s = "()[]{}" --> output == True
# s = "([])" --> output == True


def validParentheses(s: str) -> bool:
    stack = []  # stacks in python are just lists
    closeToOpen = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in closeToOpen:  # all keys of C are always a closing parentheses
            if (
                stack and stack[-1] == closeToOpen[c]
            ):  # if stack isnt empty, and the value on top of the stack is the matching opening parentheses
                print(f"popped {c} from {stack}")
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            print(f"appended {c} to {stack}")

    return True if not stack else False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False


print(validParentheses("[({})]"))
