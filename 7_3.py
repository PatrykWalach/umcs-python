

import json
import pickle


with open('7_people.json') as f:
    people = json.load(f)


with open('7_people.pkl', 'wb') as f:
    pickle.dump(people, f)
