# You are given an integer array nums of length n.
# Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).


# this is the most pythonic way -- its fucking cracked, i wrote it
def getConcatenation(nums: list[int]) -> list[int]:
    return nums + nums


# this is a more language-agnostic way to solve, probably better and same O-complexity
def getConcatenation(nums: list[int]) -> list[int]:
    loop = 0
    output = []
    while loop < 2:
        for i in range(len(nums)):
            output.append(nums[i])
        loop += 1
    return output


data = [1, 2, 3]
print(getConcatenation(data))
