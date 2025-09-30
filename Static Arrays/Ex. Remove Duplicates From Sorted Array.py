def removeDuplicates(nums: list) -> int:
    for i in nums:
        val = nums[i - 1]
        if nums.count(val) > 1:
            length = len(nums)
            for index in range(i + 1, length):
                nums[index - 1] = nums[index]
            nums.pop()
    return len(nums)


print(removeDuplicates([1, 1, 1, 2, 3]))
print(removeDuplicates([2, 10, 10, 30, 30, 30]))
