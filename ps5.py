# Create a dictionary of cities and populations
cities_population = {
    "kolhapur": 37400000,
    "pune": 29300000,
    "sangli": 26300000,
    "miraj": 21800000,
    "satara": 21600000
}
city_to_remove = "satara"
removed_population = cities_population.pop(city_to_remove, None)
print(cities_population)
