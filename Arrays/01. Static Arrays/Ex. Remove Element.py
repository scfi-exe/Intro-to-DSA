def removeElement(nums: list, val: int) -> int:
    valCount = nums.count(val)
    loopCount = 0
    while loopCount < valCount:
        nums.remove(val)
        loopCount += 1
    return len(nums)


data = [1, 1, 1, 1, 1, 2, 3, 4]
print(removeElement(data, 1))
