class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        final = []

        for x in nums2:
            if x in nums1:
                final.append(x)

        return final
