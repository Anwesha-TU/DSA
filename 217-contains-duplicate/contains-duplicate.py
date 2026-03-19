class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        count=Counter(nums)
        for c in count:
            if count[c]>1:
                return True
        return False