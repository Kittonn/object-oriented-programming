number = int(input("Input : "))

sum  = 0
temp = number
num_list = []

for i in range(4):
  num_list.append(temp)
  sum += temp
  temp = temp * 10 + number
  
print("Output : {} (={})".format(sum, "+".join([str(num) for num in num_list])))