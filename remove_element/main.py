def removeElement(nums: list[int], val: int) -> int:
        k = 0
        len_nums = len(nums)
        for i in range(0, len_nums):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

nums = [3,2,2,3]
print(removeElement(nums, 3))
print(nums)