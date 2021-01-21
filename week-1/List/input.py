from list import sorted_list

msg = '''
Give me a list of numbers and I will sort them.
Enter Numbers Here > '''

print(msg)

user_input = [int(i) for i in input('')]
print(list(user_input))

result = sorted_list(user_input)
print(result)