class Solution(object):
    def eval_binary_expr(self,op1, oper, op2):
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,  # use operator.div for Python 2
            '%' : operator.mod,
            '^' : operator.xor,
        }
        print(op1, op2, oper)
        op1, op2 = int(op1), int(op2)
        return ops[oper](op1, op2)


    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ["+", "-", "/", "*"]
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                element1 = stack.pop()
                element2 = stack.pop()
                result = self.eval_binary_expr(element2, i, element1)
                stack.append(result)

        print(stack)
        return int(stack[0])




            