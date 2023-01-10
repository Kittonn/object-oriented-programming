number = int(input())

sum  = 0
temp = number
num_list = []

for i in range(4):
  num_list.append(temp)
  sum += temp
  temp = temp * 10 + number
  
print(sum)