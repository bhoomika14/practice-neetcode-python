def contains_duplicate(nums: list) -> bool:
    """
        Given an integer array nums, return True if any valye appears at least twice in the array else False.
        arguments: List of numbers
        return: Bool (True or False)
    """
    nums_hash_set = set()
    for i in range(len(nums)):
        if nums[i] in nums_hash_set:
            return True
        nums_hash_set.add(nums[i])
    return False

print(contains_duplicate([1,2,3,1]))