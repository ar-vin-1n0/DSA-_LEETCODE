#LEETCODE -Q_1480- RUNNING SUM OF 1D ARRAY

class Solution(object):
    def runningSum(self, nums):
       numss = []
       value = 0
       for i in range(len(nums)):
           value += nums[i]
           numss.append(value)


       return numss