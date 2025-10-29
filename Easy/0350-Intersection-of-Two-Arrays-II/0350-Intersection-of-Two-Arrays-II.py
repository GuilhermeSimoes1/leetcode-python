class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        final = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                final.append(nums1[i])
                nums2.remove(nums1[i])

        return final
