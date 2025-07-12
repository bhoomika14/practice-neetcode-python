def contains_duplicate(nums: list) -> bool:
    """
        Given an integer array nums, return True if any valye appears at least twice in the array else False.
        arguments: List of numbers
        return: Bool (True or False)
    """
    nums = sorted(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

print(contains_duplicate([1,2,3,1]))