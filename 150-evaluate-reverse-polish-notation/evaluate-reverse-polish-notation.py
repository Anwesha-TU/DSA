class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=['+', '-', '*', '/']
        stk=[]
        n=len(tokens)
        for i in range (n):
            if tokens[i] not in op:
                stk.append(int(tokens[i]))
            else:
                oper1=stk.pop()
                oper2=stk.pop()
                if (tokens[i]=='+'):
                    calc=oper1+oper2
                elif (tokens[i]=='-'):
                    calc=oper2-oper1
                elif (tokens[i]=='*'):
                    calc=oper1*oper2
                elif (tokens[i]=='/'):
                    calc=int(oper2/oper1)
                stk.append(calc)
        return stk[0]