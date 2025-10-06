def removeElement(nums: list[int], val: int) -> int:
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
        else:
            pass
    return nums


print(removeElement([1, 1, 2, 3, 4], 1))  # Expected Result: [2, 3, 4]


def removeElement(nums: list[int], val: int) -> int:
    nums[:] = [i for i in nums if i != val]
    return nums


print(removeElement([1, 1, 2, 3, 4], 1))  # Expected Result: [2, 3, 4]
