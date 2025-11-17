class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        finalArray = []
        flag = 0

        for i in range(len(nums1)):

            element = nums1[i]
            indice = nums2.index(element)

            for y in range(indice, len(nums2)):

                if element < nums2[y]:
                    finalArray.append(nums2[y])
                    flag = 1
                    break

            if flag == 0:
                finalArray.append(-1)
            else:
                flag = 0

        return finalArray

