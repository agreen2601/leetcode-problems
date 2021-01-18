x = -12324829234

class Solution(object):
    def reverse(self, x):
        c = ""
        if x < 0:
            c = "-"
            x = -1 * x
        a = str(x)
        b = ""
        for i in range(len(a)):
            b = b + a[len(a)-(i+1)]
        b = c + b
        if abs(int(b)) > (2**31):
            b = 0
        print(b)
        return(int(b))
        
answer = Solution()
answer.reverse(x)