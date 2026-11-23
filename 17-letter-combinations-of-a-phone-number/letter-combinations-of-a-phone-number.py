class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits)==0:
            return []
        sol=[]
        res=[]
        let={'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        n=len(digits)
        def backtrack(i):
            if i==n:
                res.append("".join(sol))
                return
            for l in let[digits[i]]:
                sol.append(l)
                backtrack(i+1)
                sol.pop()
            return
        backtrack(0)
        return res

