class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        finalArray = []

        for i in range(len(nums1)):

            for y in range(len(nums2)):

                if nums1[i] == nums2[y]:
                    finalArray.append(nums1[i])

        finalArray = list(set(finalArray))
        return finalArray