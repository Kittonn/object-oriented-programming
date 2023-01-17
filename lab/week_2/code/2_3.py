def delete_minus(nums):
  return [list(filter(lambda item: item >= 0, num)) for num in nums]
