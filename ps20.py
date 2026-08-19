data_with_duplicates = {
    "apple": "fruit",
    "carrot": "vegetable",
    "banana": "fruit",
    "broccoli": "vegetable",
    "chicken": "meat"
}
cleaned_data = {}
seen_values = set()

for key, value in data_with_duplicates.items():
    if value not in seen_values:
        cleaned_data[key] = value
        seen_values.add(value)

print(cleaned_data)
