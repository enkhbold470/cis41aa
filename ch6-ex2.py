"""
# Inky Ganbold
# CIS41A
# Chapter 6 Exercise 2
# Team: Python Enjoyers
# This program manages a dictionary of friends met in 2017 and 2018.
# It allows users to search for friends, add new friends to specific years,
# and displays the updated dictionary.
"""

# Create initial dictionary with friends from 2017 and 2018
friend_dict = {'2017': ["Joe", "Lily", "Sarah"], '2018': ["Bob", "Tom", "Alex"]}

print("=== Friends Dictionary Manager ===\n")

# Display current friends
print("Current friends:")
for year, friends in friend_dict.items():
    print(f"{year}: {', '.join(friends)}")

print()

# Ask user to search for a friend
search_name = input("Enter the name of a friend to search for: ").strip()

# Search for the friend in both years
found_year = None
for year, friends in friend_dict.items():
    if search_name in friends:
        found_year = year
        break

if found_year:
    print(f"Found {search_name} in {found_year}!")
else:
    print(f"{search_name} was not found in your friends list.")

print()

# Ask user to add a new friend
new_friend = input("Enter the name of a new friend to add: ").strip()

# Ask for the year to associate with this friend
while True:
    year_choice = input("Which year did you meet this friend? (2017 or 2018): ").strip()
    if year_choice in ['2017', '2018']:
        break
    else:
        print("Please enter either '2017' or '2018'.")

# Add the new friend to the appropriate list
friend_dict[year_choice].append(new_friend)

print(f"\n{new_friend} has been added to {year_choice}!")

# Display the updated dictionary
print("\nUpdated friends dictionary:")
for year, friends in friend_dict.items():
    print(f"{year}: {friends}")

"""
Sample Output 1:
=== Friends Dictionary Manager ===

Current friends:
2017: Joe, Lily, Sarah
2018: Bob, Tom, Alex

Enter the name of a friend to search for: Joe
Found Joe in 2017!

Enter the name of a new friend to add: Maria
Which year did you meet this friend? (2017 or 2018): 2018

Maria has been added to 2018!

Updated friends dictionary:
2017: ['Joe', 'Lily', 'Sarah']
2018: ['Bob', 'Tom', 'Alex', 'Maria']

Sample Output 2:
=== Friends Dictionary Manager ===

Current friends:
2017: Joe, Lily, Sarah
2018: Bob, Tom, Alex

Enter the name of a friend to search for: Kevin
Kevin was not found in your friends list.

Enter the name of a new friend to add: David
Which year did you meet this friend? (2017 or 2018): 2017

David has been added to 2017!

Updated friends dictionary:
2017: ['Joe', 'Lily', 'Sarah', 'David']
2018: ['Bob', 'Tom', 'Alex']
"""
