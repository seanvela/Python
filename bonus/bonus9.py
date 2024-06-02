# program to ask user to enter password
# check if there is at least 8 characters
# check if there is at least 1 number
# check if there is at least 1 uppercase
# check if password is strong

# prompt user
password = input('Enter a new password: ')

# dictionary to save passwords
result = {}

# check if password is greater than 8 characters
if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

# check if password has one number
digit = False
for i in password:
    if i.isdigit():
        digit = True

# add to dict
result["digit"] = digit

# check if there is at least one uppercase
uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

# add to dict
result['uppercase'] = uppercase

print(result)

# check if password is strong
if all(result):
    print('Strong password')
else:
    print('Weak password')