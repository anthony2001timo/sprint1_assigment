import csv

# Define helper function to check if a name is a palindrome
def is_palindrome(name):
    return name == name[::-1]

# Initialize variables
yearly_count = {}
shortest_name = ""  # Initialize as an empty string
longest_name = None
palindromes = []
name_count = {}

# Read the CSV file
with open("/content/registered-names-1922-2015.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    # Process each row in the CSV file
    for row in reader:
        name = row['name']
        year = row['year']

        # Skip rows where 'name' is empty or invalid
        if not name:
            continue

        # Count people registered each year
        if year in yearly_count:
            yearly_count[year] += 1
        else:
            yearly_count[year] = 1

        # Track the shortest and longest name
        if len(name) < len(shortest_name) or shortest_name == "":
            shortest_name = name
        if longest_name is None or len(name) > len(longest_name):
            longest_name = name

        # Check if the name is a palindrome
        if is_palindrome(name):
            palindromes.append(name)

        # Track the number of people with each name
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1

# Find the name with the largest number of people registered
most_common_name = max(name_count, key=name_count.get)
most_common_name_count = name_count[most_common_name]

# Output results
print(f"People registered each year:")
for year, count in sorted(yearly_count.items()):
    print(f"{year}: {count} people")

print(f"\nThe shortest name in the dataset is: {shortest_name}")
print(f"The longest name in the dataset is: {longest_name}")

print(f"\nPalindrome names in the dataset: {palindromes}")

print(f"\nThe name with the largest number of people registered is: {most_common_name} ({most_common_name_count} registrations)")
