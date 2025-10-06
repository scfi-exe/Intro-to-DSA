# READING FROM AN ARRAY
# initialize myArray
myArray = [1, 3, 5]

# access an arbitrary element, where i is the index of the desired value
# myArray[i]
myArray[0]


# TRAVERSING AN ARRAY
for i in range(len(myArray)):
    print(myArray[i])

# OR

i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1


# DELETING FROM AN ARRAY
# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr):
    length = len(arr)
    if length > 0:
        # Overwrite last element with some default value.
        # We would also consider the length to be decreased by 1.
        arr[length - 1] = 0
    return arr


# In a statically-typed language, setting it to 0 might actually "pop" it from the array.
# In Python, it just sets the actual value to 0 (which, depending on the dataset, could be used to represent "null")
print(removeEnd(myArray))


# DELETING AT THE iTH INDEX
# 1. We are given the deletion index, i
# 2. We iterate starting from i+1 until the end of the array
# 3. We shift each element 1 position to the left
# 4. (Optional) We replace the last element with a 0 or null to mark it empty, and decrement the length by 1
# Below code removes value at index, i, before shifting elements to the left (assuming i is a valid index)
def removeMiddle(arr, i, length):
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    arr.pop()  # I added this line to comply with step 4
    return arr


print(removeMiddle([1, 2, 3, 4, 5], 2, 5))


# INSERTION - INSERTING AT THE END
# IF
