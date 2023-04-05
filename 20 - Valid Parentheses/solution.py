class mySolution:
    def isValid(self, s: str) -> bool:

        parentheses_count = 0
        curly_count = 0
        bracket_count = 0

        for c in s:
            if c == '(' or c == ')':
                parentheses_count += 1
            elif c == '{' or c == '}':
                curly_count += 1
            elif c == '(' or c == ')':
                bracket_count += 1
        if parentheses_count % 2 == 0 and curly_count % 2 == 0 and bracket_count % 2 == 0:
            return True

        return False

#solution from https://leetcode.com/problems/valid-parentheses/solutions/2411675/very-easy-100-fully-explained-c-java-python-js-python3/

class PratikSen07_Solution:
    def isValid(self, s: str) -> bool:
        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0