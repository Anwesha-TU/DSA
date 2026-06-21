class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        i=0
        low=i+1
        high=n-1
        ans=[]
        for i in range (n):
            if nums[i]>0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low=i+1
            high=n-1
            while (low<high):
                    if nums[low]+nums[high]+nums[i]==0:
                        sol=[nums[i], nums[low], nums[high]]
                        # if sol not in ans:
                        ans.append(sol)
                        low+=1
                        high-=1
                        while low < high and nums[low] == nums[low - 1]:
                            low+=1
                        while low < high and nums[high] == nums[high+ 1]:
                            high-=1
                    elif nums[low]+nums[high]+nums[i]>0:
                        high-=1
                    else:
                        low+=1
        return ans