# Accept string from the user
user_string = input("Enter a string: ")
frequency_dict = {}
for char in user_string:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1
print("Character frequencies:")
print(frequency_dict)
