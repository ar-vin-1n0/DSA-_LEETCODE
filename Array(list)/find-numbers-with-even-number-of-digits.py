#LEETCODE - Q_1295 - find-numbers-with-even-number-of-digits

class Solution(object):
    def findNumbers(self, nums):
       result = 0
       for i in nums:
          if len(str(i)) % 2 == 0:
            result += 1
       return result

nums = []
solution = Solution()
solution.findNumbers(nums)

