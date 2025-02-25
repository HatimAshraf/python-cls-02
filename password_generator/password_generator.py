
#generate password based on user style
# - length
# - uppercase
# - lowercase
# - digits
# - special characters    
import random
import string
def generate_password():
  length = int(input("Enter the length of the password: "))
  if length < 4:
    print("password length must be at least more than 4 characters")
    return
  uppercase = input("Do you want uppercase letters? (y/n): ").strip().lower()
  lowercase = input("Do you want lowercase letters? (y/n): ").strip().lower()
  digits = input("Do you want digits? (y/n): ").strip().lower()
  special_chars = input("Do you want special characters? (y/n): ").strip().lower()

  
  
  uppercase_letters = string.ascii_uppercase if uppercase == 'y' else ''
  lowercase_letters = string.ascii_lowercase if lowercase == 'y' else ''
  digits_chars = string.digits if digits == 'y' else ''
  special_chars_set = string.punctuation if special_chars == 'y' else ''

  all_chars = uppercase_letters + lowercase_letters + digits_chars + special_chars_set
  # print(all_chars)

  password = ''
  for _ in range(length):
    password += random.choice(all_chars).strip()                 


  # password = ''.join(random.choice(all_chars) for _ in range(length))
  print(password)

generate_password()
