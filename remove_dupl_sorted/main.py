j = 1

nums = [1, 1, 2, 2, 3]

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[j] = nums[i]
        j += 1
print(j)