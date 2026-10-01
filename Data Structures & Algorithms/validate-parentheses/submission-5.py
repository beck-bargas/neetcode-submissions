class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        stack = []

        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            elif len(stack) and stack[-1] == closing[c]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True

        

        