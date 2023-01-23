def count_minus(num):
  return len([item for item in list(map(int, num.split())) if item < 0])