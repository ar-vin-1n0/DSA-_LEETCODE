class Solution(object):
    def numIdenticalPairs(self, nums):
        freq = {}
        pairs = 0
        for n in nums:

            if n in freq:
                pairs += freq[n]
                freq[n] += 1
            else:
                freq[n]=1
        return pairs              
