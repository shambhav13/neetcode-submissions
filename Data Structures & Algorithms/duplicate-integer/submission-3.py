class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hshmap=set()
        for num in nums:
            if num in hshmap:
               return True
            hshmap.add(num)
        return False



