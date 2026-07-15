class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            flag=0
            if nums[l]<=nums[mid]:
                flag=1
            if target==nums[mid]:
                return mid
            elif flag == 1 and nums[l] <= target < nums[mid]:
                r = mid - 1

            elif flag == 1:
                l = mid + 1

            elif flag == 0 and nums[mid] < target <= nums[r]:
                l = mid + 1

            elif flag == 0:
                r = mid - 1
        return -1