ops = ["5", "2", "C", "D", "+"]
ops = ["5","-2","4","C","D","9","+","+"]
new = []
# Output: 30


class Solution(object):
    def calPoints(self, ops):
        total = 0
        for i in range(len(ops)):
            if ops[i] == "+":
                new.append(int(new[len(new)-1]) + int(new[len(new)-2]))
            elif ops[i] == "D":
                new.append(2 * int(new[len(new)-1]))
            elif ops[i] == "C":
                new.pop()
            else:
                new.append(int(ops[i]))
            print(new)
        for j in range(len(new)):
            total = total + new[j]
            print(total)
        return total

answer = Solution()
answer.calPoints(ops)