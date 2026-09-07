class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshmap={}
        for i,num in enumerate(nums):
            need=target-num
            if need in hshmap:
                return[hshmap[need],i]
            hshmap[num]=i