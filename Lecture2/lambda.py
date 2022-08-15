from this import d


people = [
    { "name": "B", "house": "CHouse"},
    { "name": "A", "house": "BHouse"},
    { "name": "C", "house": "AHouse"},
]

# def f(person):
#     return person["house"]

# people.sort(key=f)

people.sort(key=lambda person: person["name"])
print(people)