nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

class Solution:
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        print(nums)
        return nums
        
answer = Solution()
answer.sortedSquares(nums)
