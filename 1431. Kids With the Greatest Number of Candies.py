candies = [2,3,5,1,3]
extraCandies = 3
# Output: [true,true,true,false,true]

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        possible = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                possible[i] = True
            else :
                possible[i] = False
        print(possible)
        return possible
        
answer = Solution()
answer.kidsWithCandies(candies, extraCandies)
