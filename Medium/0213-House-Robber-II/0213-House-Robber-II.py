class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[:-1]
        nums2 = nums[1:]

        lenghtNums1 = len(nums1)
        lenghtNums2 = len(nums2)

        valueHouses1 = [0] * lenghtNums1
        valueHouses2 = [0] * lenghtNums2

        if lenghtNums1 == 1 and lenghtNums2 == 1:
            return max(nums1[0], nums2[0])

        if lenghtNums1 == 1:
            return nums1[0]
        else:
            valueHouses1[0] = nums1[0]
            valueHouses1[1] = max(nums1[0], nums1[1])

            for i in range(2, lenghtNums1):
                valueHouses1[i] = max(valueHouses1[i - 1], nums1[i] + valueHouses1[i - 2])

        if lenghtNums2 == 1:
            return nums2[0]
        else:
            valueHouses2[0] = nums2[0]
            valueHouses2[1] = max(nums2[0], nums2[1])

            for i in range(2, lenghtNums2):
                valueHouses2[i] = max(valueHouses2[i - 1], nums2[i] + valueHouses2[i - 2])

        return max(valueHouses1[-1], valueHouses2[-1])  