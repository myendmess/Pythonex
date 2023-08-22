people = [
    {"name": "Walther", "orientation": "Neutral"},
    {"name": "Jesse", "orientation": "Good"},
    {"name": "Saul", "orientation": "Lawyer"},
    {"name": "Todd", "orientation": "Evil"}
]

# Python doesn't know how to sort these, so we shall use a function to instruct it


people.sort(key=lambda person: person ["name"]) #this is a complete function!

print(people)
