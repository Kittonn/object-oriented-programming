string = input("Enter a string : ")

lower_count = len([char for char in string if char.islower()])
upper_count = len([char for char in string if char.isupper()])

print(f"{lower_count}\n{upper_count}")
