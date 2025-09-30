def removeDuplicates(nums: list) -> int:
    unique = sorted(set(nums))
    nums[: len(unique)] = unique
    return unique


print(removeDuplicates([1, 1, 1, 3, 2, 3, 3, 2, 3, 2]))
