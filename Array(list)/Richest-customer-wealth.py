#LEETCODE - Q_1672 - richest customer wealth

class Solution(object):
    def maximumWealth(self, accounts):
        result = 0
        for n in accounts:
            wealth = 0
            for i in n:
                wealth += i

            result = max(result, wealth)

        return result


accounts = []
solution = Solution()
solution.maximumWealth(accounts)
