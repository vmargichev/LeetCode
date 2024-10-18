class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        max = m + n
        del nums1[m:max]

        for num in nums2:
            nums1.append(num)

        for i in range(0, max - 1):
            swapped = False
            for j in range(0, max-i-1):
                if nums1[j] > nums1[j + 1]:
                    swapped = True
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
            if not swapped:
                break
