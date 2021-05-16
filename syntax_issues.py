#1 https://openclassrooms.com/en/courses/6902811-learn-python-basics/7090471-store-groups-of-data-using-lists#/id/r-7091736
social_platforms = ["Instagram", "Facebook",  "Snapchat", "Twitter"]
# issue: sort(social_platforms)
# what actually works:
social_platforms.sort()
print(social_platforms)

#2 https://openclassrooms.com/en/courses/6902811-learn-python-basics/7090571-store-complex-data-with-dictionaries#/id/r-7092863
golden_doodle_facts = {
    "mass": "30-35 lbs.",
    "origin": "United States",
    "scientific_name": "Canis lupus familiaris"
}
# issue del golden_doodle_facts[“origin”]
# what actually works:
#  (typing it out yourself)
del golden_doodle_facts["origin"]

#3 https://openclassrooms.com/en/courses/6902811-learn-python-basics/7091381-load-data-with-python#/id/r-7091864
# issue:  print row
# what actually works:
# print (row)