def removeDuplicates(nums: list[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)


nums = [1, 1, 1, 2, 2, 3, 4]
print(removeDuplicates(nums))  # Expected Result: 4
