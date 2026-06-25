#LEETCODE - Q_1 - TWO SUM


class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                   return [i,j]


nums = [3,4,5,6,7]
target = 10

solution = Solution()
print(solution.twoSum(nums, target))