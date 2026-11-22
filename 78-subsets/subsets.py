class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result,sol=[],[]
        def backtrack(i):
            if i==n:
                result.append(sol[:])
                return
            
            #Dont pick nums[i]
            backtrack(i+1)

            #Pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            
        
        backtrack(0)
        return result