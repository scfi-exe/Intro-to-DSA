def isValid(self, s: str) -> bool:
    stack = []
    closeToOpen = {")": "(", "}": "{", "]": "["}
    for i in stack:
        if i in closeToOpen:
            if stack and closeToOpen[-1] == i:
                closeToOpen.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False