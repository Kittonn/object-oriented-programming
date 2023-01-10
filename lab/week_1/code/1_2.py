string = input("Enter a string : ")

lower_count = upper_count = 0

for char in string:
  if char.islower():
    lower_count += 1
  elif char.isupper():
    upper_count += 1

print(f"{lower_count}\n{upper_count}")
