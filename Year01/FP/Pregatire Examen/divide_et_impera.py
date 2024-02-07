from random import shuffle


def no_of_negatives(nums, left, right):
    if len(nums) == 0:
        raise ValueError("Empty list")
    if left == right:
        if nums[left] < 0:
            return 1
        else:
            return 0

    middle = (left + right) // 2
    left_side = no_of_negatives(nums, left, middle)
    right_side = no_of_negatives(nums, middle + 1, right)
    return left_side + right_side


def maximum(nums, left, right):
    if len(nums) == 0:
        raise ValueError("Empty list")
    if left == right:
        return nums[left]

    middle = (left + right) // 2
    left_side = maximum(nums, left, middle)
    right_side = maximum(nums, middle + 1, right)
    return max(left_side, right_side)


def atLeastOneEven(nums, left, right):
    if len(nums) == 0:
        raise ValueError("Empty List")

    if left == right:
        return nums[left] % 2 == 0

    middle = (left + right) // 2
    return atLeastOneEven(nums, left, middle) or atLeastOneEven(nums, middle + 1, right)


def inverseList(nums, left, right):
    if len(nums) == 0:
        raise ValueError("Empty list")

    if left == right:
        return [nums[left]]

    middle = (left + right) // 2
    left_side = inverseList(nums, left, middle)
    right_side = inverseList(nums, middle + 1, right)
    return right_side + left_side

def evenIndexedProduct(nums, left, right):
    if len(nums) == 0:
        raise ValueError("Empty list")

    if left == right:
        if left % 2 == 0:
            return nums[left]
        else:
            return 1


    middle = (left + right) // 2
    left_side = evenIndexedProduct(nums, left, middle)
    right_side = evenIndexedProduct(nums, middle + 1, right)
    return left_side * right_side

def dubled(nums, left, right):
    if len(nums) == 0:
        raise ValueError("Empty list")

    if left == right:
        return [nums[left] * 2]


    middle = (left + right) // 2
    left_side = dubled(nums, left, middle)
    right_side = dubled(nums, middle + 1, right)
    return left_side + right_side


nums = [123, 2, 932, -6, 4, 3, 1, -90, -98, 123, 0, 325, 9, -2]
nums2 = [1, 3, 5, 7, 9, 11, -11, -9, -5, 2]
nums3 = [1,2,3,4,5, 0, -3]

print(dubled(nums3, 0, len(nums3) - 1))
