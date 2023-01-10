num = int(input("Input : "))

sum  = 0
temp = num
num_list = []

for i in range(4):
  num_list.append(temp)
  sum += temp
  temp = temp * 10 + num
  
print("Output : {} (={})".format(sum, "+".join([str(i) for i in num_list])))