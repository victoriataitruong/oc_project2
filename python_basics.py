""" 
variable declaration:
a variable name cannot start with a number,
one of the popular naming conventions for Python is called snake case — names made up of multiple words with underscores between the words, e.g.,  number_of_cats
""" 
book = "The Great Gatsby"

# printing out a variable
print (book)

# renaming a variable
book = "Beloved"

"""
The most basic, or primitive, data types used in Python are:
Integers, Floats, Strings, Booleans

Numeric types can fall into two categories in Python: integer or float.
"""

# boolean examples
sunny_weather = True
sunny_weather = False

"""
lists example 
lists can use any other type of data as well, or even any combination of data type

to access elements in a list, you use an index. Each element has an index related to it, depending on its position in the list. You get the value at that index with the following syntax: list[index]  , which will give you the value in the list at that index.
The important thing to note here is that in most programming languages, including Python, indices start at 0, not 1. 
In Python specifically, you can also access elements backward using negative numbers. To get the last element of a list, use the -1 index.
Strings can be indexed, too! In fact, Python strings are really just lists of characters. Each character is given an index from zero to the length of the string.
"""

social_platforms = ["Facebook", "Instagram", "Snapchat", "Twitter"]
print (social_platforms[0])
print (social_platforms[-1])

"""
Python makes it easy to do all sorts of operations on lists. Instead of creating a whole new list every time you want to add, remove, or sort it, you can call a list method. For example, if you want to add a social media platform to the end of the existing list, you can use the  append()  method. To remove a specific element from a list, you can use the .remove()method. To find out the length of the list, use the len() method. The last method we'll look at is sort(), which will sort the elements of a list. This will work alphabetically for lists of strings, and numerically for lists of numbers.
"""
social_platforms.append("TikTok")
print(social_platforms)
social_platforms.remove("Snapchat")
print(len(social_platforms))
social_platforms.sort()

"""
Tuples are another Python structure that can be used to store data, although instead of brackets [], they are defined using parentheses ().  The main difference is that tuples are immutable (can't be modified), while lists are mutable (can be modified).
"""
social_platforms_tuple = ("Facebook", "Instagram", "TikTok", "Twitter")

"""
A dictionary is a data structure that stores data in key-value pairs.  An example of a key and a value is campaign_manager: "Spencer Smith" where  campaign_manager  is the key, and  Spencer Smith  is the value. You can also create a new dictionary with just empty curly brackets  {}  or the  dict() function and add key-value pairs in after. To access the different values, you can use the key for any one of the key-value pairs.
"""
new_campaign = {
    "campaign_manager": "Spencer Smith",
    "campaign_name": "We love dogs campaign",
    "start_date": "01/01/2020",
    "end_date": "01/01/2021",
    "relevant_influencers": ["@MyDogLover", "@DogFoodFavorites"]
}
conversion_rates = {}
conversion_rates['facebook'] = 3.4
conversion_rates['instagram'] = 1.2

conversion_rates = dict()
conversion_rates['facebook'] = 3.4
conversion_rates['instagram'] = 1.2

new_campaign['campaign_manager']
"Spencer Smith"

"""
To add a key-value pair to a dictionary, just add a new key to the existing dictionary. If the key already exists, setting a value will overwrite the existing key. The following code creates a dictionary called  golden_doodle_facts  and saves information about the mass and origin of the Goldendoodle dog breed. To delete a key-value pair, you can use the  del  keyword and the key you want to delete.  
"""
golden_doodle_facts = {
    "mass": "30-35 lbs.",
    "origin": "United States"
}

golden_doodle_facts['scientific_name'] = "Canis lupus familiaris"
del golden_doodle_facts["origin"]

"""
Certain words are part of the Python language and can’t be used when naming variables.  Examples are del,if, and else. Such words are known as reserved words or keywords

You can use the  in  keyword to check whether a specific key exists in a dictionary. To do this, specify the key you want to search for, the keyword  in  , and the name of the dictionary variable to search. The result will be a boolean indicating whether or not the key is in that dictionary. 
"""
print("mass" in golden_doodle_facts)

"""
An if/elif/else statement allows you to define multiple conditions. The elif keyword allows you to add as many conditions as you’d like. You then end the statement with an else clause.
If you want to check multiple conditions for a single outcome in the same if statement, you can use logical operators:
and : check if two conditions are both true.
or : check if at least one condition is true.
not: check if a condition is not true (i.e., false). 
These operators can be mixed and matched for your needs.
"""
sunny = False
snowing = True
if sunny:
    print("go to the beach!")
elif snowing:
    print("build a snowman")
else:
    print("stay inside!")

is_sunny = True
is_weekday = False

if is_sunny and not is_weekday:
    print("go to the beach!")
elif is_sunny and is_weekday:
    print("go to work")
else:
    print("stay inside!")

"""
Comparative expressions let you compare different expressions to each other and evaluate whether that expression is true or false.
If you have two values a and b, you can use the following comparison operators in Python: 
Equals: a  ==  b
Not Equals: a  !=  b
Less than: a  <  b
Less than or equal to: a  <=  b
Greater than: a  >  b
Greater than or equal to: a  >=  b 
"""

number_of_seats = 30
number_of_guests = 25

if number_of_guests < number_of_seats:
    print()
else: 
    print()

"""
The for loop is the core type of looping in Python. A  for  loop is used to iterate over any sequence. That can be a list, tuple, dictionary, or even a string. With a  for  loop, you can execute the same code for each element in that sequence. 
"""
dog_breeds = ["golden retriever", "chihuahua", "terrier", "pug"]
for dog in dog_breeds:
    print(dog)

"""
To loop through a set of code a certain number of times, you can use the  range()  function, which returns a list of numbers starting from 0 to the specified end number
"""
for x in range(5):
    print(x)
for x in range(100):
    print(f"{x} bottles of beer on the wall!")

"""
The code snippet below checks the current capacity and increases it by 1 until the maximum capacity is reached (+= 1 increases the current value by 1).
"""
maximum_capacity = 10
current_capacity = 3

while current_capacity <= maximum_capacity:
    current_capacity += 1

"""
Think of a function as a way to reuse a repeatable set of instructions. You define it using the  def keyword, the name of the function, parentheses, and a colon  :. If the function requires one or more parameters, they go inside the parentheses separated by commas. 
"""
def add(a, b):
    return a + b

print(add(4,5))

