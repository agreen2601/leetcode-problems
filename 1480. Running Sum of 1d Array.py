nums= [1, 2, 3, 4]

class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        print(nums)
        return nums
        
answer = Solution()
answer.runningSum(nums)