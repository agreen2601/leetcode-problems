points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# points = [[8,7],[9,9],[7,4],[9,7]]

Output: 3

class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        dist = []
        points.sort()
        for j in range(1, len(points)):
            dist.append(abs(points[j][0] - points[j-1][0]))
        a = max(dist)
        return(a)

        
answer = Solution()
answer.maxWidthOfVerticalArea(points)

# class Solution(object):
#     def maxWidthOfVerticalArea(self, points):
#         x = sorted(x for x, y in points)
#         print(max(x2 - x1 for x1, x2 in zip(x, x[1:])))
#         return max(x2 - x1 for x1, x2 in zip(x, x[1:]))

# a = Solution()
# a.maxWidthOfVerticalArea(points)