palindrome_list = []


def check_palindrome(num: str):
  return num == num[::-1]


for first_number in range(999, 99, -1):
  for second_number in range(999, 99, -1):
    num = first_number * second_number
    if (check_palindrome(str(num))):
      palindrome_list.append(num)

print(max(palindrome_list))
