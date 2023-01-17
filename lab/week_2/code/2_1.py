from itertools import permutations

num = list(map(int, input().split()))[:10]

for item in sorted(permutations(num, len(num))):
  item = "".join(map(str, item))
  if item[0] != "0":
    print(item)
    break
