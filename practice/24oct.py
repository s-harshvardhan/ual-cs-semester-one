class Solution(object):
    def twoSum(self, nums, target):
        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """
        rtype = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if j!=i:
                    if nums[i]+nums[j] == target:
                        rtype.extend([i, j]) 
        return print(rtype[:2])

nums = [3,3] 
target = 6
x = Solution()
x.twoSum(nums, target)
