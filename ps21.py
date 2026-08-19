# 1. Create an unsorted dictionary
my_dict = {
    'banana': 3,
    'apple': 5,
    'cherry': 2,
    'date': 4
}
for key in sorted(my_dict.keys()):
    print(f"{key}: {my_dict[key]}")
