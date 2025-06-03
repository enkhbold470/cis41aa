# ~~~ Inky Ganbold ~~~
# CIS 41
# This program is a rad way to rock two friend lists from 2017 and 2018.
# It shows you the ultimate merged list, hunts down your crew, and lets you add new pals!

## == Initialize Legendary Friend Crews for 2017 & 2018 == ##
friends_2017 = ["Joe", "Lily", "Sarah", "Mike"]
friends_2018 = ["Bob", "Tom", "Anna", "Chris"]

## == Combine the Crews and Reveal the Legendary Lineup == ##
combined_friends = friends_2017 + friends_2018
print(">>> Revealing the Ultimate Friends Roster (2017 + 2018):")
print(combined_friends)
print()

## == Seek Out a Friend: Enter the Name of Your Buddy to Search == ##
search_name = input(">>> Type the name of a friend to hunt for: ")

## == Check the Crews - Is Your Buddy Among the Legends? == ##
if search_name in friends_2017:
    print(f">>> Boom! {search_name} is rocking the 2017 squad!")
elif search_name in friends_2018:
    print(f">>> Whoa! {search_name} is rollin' with the 2018 crew!")
else:
    print(f">>> Oops! {search_name} didn't make the cut for 2017 or 2018.")
print()

## == Amp Up the Crew - Add a Hotshot New Friend == ##
new_friend = input(">>> Enter the name of a new legend to join the crew: ")
year = input(">>> Which year? (enter 2017 or 2018): ")

## == Insert the New Legend into the Proper Squad == ##
if year == "2017":
    friends_2017.append(new_friend)
    print(f">>> Rad move! {new_friend} is now part of the 2017 crew!")
elif year == "2018":
    friends_2018.append(new_friend)
    print(f">>> Awesome! {new_friend} has joined the 2018 squad!")
else:
    print(">>> Hold up! Invalid year. Please use 2017 or 2018.")
print()

## == Final Roll Call - Display the Updated Crews == ##
print(">>> Here’s your updated crew status:")
print(f"2017 legends: {friends_2017}")
print(f"2018 legends: {friends_2018}")

"""
Sample Output 1:
>>> Revealing the Ultimate Friends Roster (2017 + 2018):
['Joe', 'Lily', 'Sarah', 'Mike', 'Bob', 'Tom', 'Anna', 'Chris']

>>> Type the name of a friend to hunt for: Joe
>>> Boom! Joe is rocking the 2017 squad!

>>> Enter the name of a new legend to join the crew: Emma
>>> Which year? (enter 2017 or 2018): 2018
>>> Awesome! Emma has joined the 2018 squad!

>>> Here’s your updated crew status:
2017 legends: ['Joe', 'Lily', 'Sarah', 'Mike']
2018 legends: ['Bob', 'Tom', 'Anna', 'Chris', 'Emma']

Sample Output 2:
>>> Revealing the Ultimate Friends Roster (2017 + 2018):
['Joe', 'Lily', 'Sarah', 'Mike', 'Bob', 'Tom', 'Anna', 'Chris']

>>> Type the name of a friend to hunt for: Alex
>>> Oops! Alex didn't make the cut for 2017 or 2018.

>>> Enter the name of a new legend to join the crew: David
>>> Which year? (enter 2017 or 2018): 2017
>>> Rad move! David is now part of the 2017 crew!

>>> Here’s your updated crew status:
2017 legends: ['Joe', 'Lily', 'Sarah', 'Mike', 'David']
2018 legends: ['Bob', 'Tom', 'Anna', 'Chris']
"""