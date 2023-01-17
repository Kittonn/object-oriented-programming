def count_minus(num):
  num = list(map(int, num.split()))
  return len([item for item in num if item < 0])
