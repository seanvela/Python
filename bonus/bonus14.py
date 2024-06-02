from parser14 import parse
from converter14 import convert

# if files are in different folder use following format: bonus.parser14

feet_inches = input('Enter feet and inches: ')


parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 1:
    print('Kid is too small.')
else:
    print('Kid can use slide')

