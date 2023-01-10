string = input("Enter a string : ")

lower_count = upper_count = 0

for char in string:
  if char.islower():
    lower_count += 1
  elif char.isupper():
    upper_count += 1

print(f"Lower case: {lower_count}\nUpper case: {upper_count}")
