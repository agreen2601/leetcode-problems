nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# Output: [1,2,2,3,5,6]

class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1 = nums1[:m] + nums2
        nums1.sort()
        print(nums1)
        
answer = Solution()
answer.merge(nums1, m, nums2, n)