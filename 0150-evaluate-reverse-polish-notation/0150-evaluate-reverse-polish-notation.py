class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                result = None
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    result = num2 + num1
                elif token == "-":
                    result = num2 - num1
                elif token == "*":
                    result = num2 * num1
                elif token == "/":
                    result = int(num2 / num1)
                stack.append(result)
        return stack[-1]
                