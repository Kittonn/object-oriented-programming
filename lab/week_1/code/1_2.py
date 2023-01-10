strings = input("Enter a string : ")

lower_count = upper_count = 0

for i in strings:
  if i.islower():
    lower_count += 1
  elif i.isupper():
    upper_count += 1

print(f"Lower case: {lower_count}\nUpper case: {upper_count}")
