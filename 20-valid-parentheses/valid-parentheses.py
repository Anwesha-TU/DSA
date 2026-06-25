class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for op in s:
            if (op=='(') or (op=='{') or (op=='['):
                stk.append(op)
            else:
                if not stk:
                    return False
                if (op==')'):
                    if (stk[-1]!='('):
                        return False
                elif (op=='}'):
                    if (stk[-1]!='{'):
                        return False
                elif (op==']'):
                    if (stk[-1]!='['):
                        return False
                stk.pop()
        return (len(stk)==0)