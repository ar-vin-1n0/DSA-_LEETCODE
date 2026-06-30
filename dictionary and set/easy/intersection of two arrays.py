class Solution:
    def intersection(self, nums1, nums2):

        unique = set(nums1)
        result = set()

        for i in nums2:
            if i in unique:
                result.add(i)

        return list(result)