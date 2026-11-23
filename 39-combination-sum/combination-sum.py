class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        sol=[]
        def backtrack(i,cur_sum):
            if cur_sum==target:
                res.append(sol[:])
                return
            if cur_sum>target:
                return
            if i==len(candidates):
                return
            backtrack(i+1,cur_sum)
            sol.append(candidates[i])
            backtrack(i,cur_sum+candidates[i])
            sol.pop()
            return
        backtrack(0,0)
        return res