palindrome_list = []

def check_palindrome(num : str):
  return num == num[::-1]

for i in range(999,99, -1):
  for j in range(999,99, -1):
    num = i * j
    palindrome_list.append(num)
    
print(f"The largest palindrome : {max(palindrome_list)}")
    
  