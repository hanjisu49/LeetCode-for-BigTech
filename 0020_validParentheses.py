class Solution:
    def isValid(self, s: str) -> bool:
    
        if len(s) % 2 == 1:
            return False

        dic = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if c in dic:	# = for c in dic.keys()
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False