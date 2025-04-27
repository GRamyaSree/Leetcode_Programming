class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=set(nums)
        small=1
        while small in num:
            small+=1
        return small