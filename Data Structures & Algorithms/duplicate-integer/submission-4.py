class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hshmap=set()
        for number in nums:
            if number in hshmap:
                return True
            hshmap.add(number)
        return False