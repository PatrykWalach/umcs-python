import json


if __name__ == '__main__':
    with open('7_people.json') as f:
        people = json.load(f)

    try:
        while True:
            print('D-Delete')
            print('A-Add')
            for person in people:
                print(person)
            c = input('')
            if c == 'D':
                people.pop(int(input('index:')))
            if c == 'A':
                f_name = input('f_name:')
                l_name = input('l_name:')
                age = input('age:')
                mynums = input('mynums (csl):')
                p = {
                    'f_name': f_name,
                    'l_name': l_name,
                    'age': int(age),
                    'mynums': [int(n) for n in mynums.split(',')]
                }
                people.append(p)
    except KeyboardInterrupt:
        pass

    with open('7_people.json', 'w') as f:
        json.dump(people, f)
