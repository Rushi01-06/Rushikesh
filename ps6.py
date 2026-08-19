# Create a dictionary of employee IDs (keys) and names (values)
employees = {
    "E101": "sid g",
    "E102": "yash g",
    "E103": "harsh p",
    "E104": "parth s"
}
search_id = input("Enter the Employee ID to look up: ").strip()
if search_id in employees:
    print(f"Match found! Employee ID {search_id} belongs to {employees[search_id]}.")
else:
    print(f"Employee ID {search_id} does not exist in our records.")
