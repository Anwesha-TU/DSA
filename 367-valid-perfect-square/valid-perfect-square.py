class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root=int(num**0.5)
        perfect_sq=root*root
        return (perfect_sq==num)