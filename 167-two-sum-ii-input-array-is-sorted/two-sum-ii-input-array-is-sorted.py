class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l=0
        r=n-1
        for i in range (n):
            while l<r:
                s = numbers[l] + numbers[r]
                diff=target-numbers[l]
                if numbers[r]==diff:
                    return [l+1,r+1] 
                elif (s<target):
                    l+=1
                else:
                    r-=1