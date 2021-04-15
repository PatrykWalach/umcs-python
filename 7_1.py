import json

people = [
    {'f_name': 'Thando', 'l_name': 'Linda', 'age': 65, 'mynums': [13]},
    {'f_name': 'Sven', 'l_name': 'Laila', 'age': 34, 'mynums': [3, 7]},
    {'f_name': 'Gergina', 'l_name': 'Ram', 'age': 21, 'mynums': [10]}
]


with open('7_people.json', 'w+') as f:
    f.write(json.dumps(people))
