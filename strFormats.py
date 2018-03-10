import requests
import json

person = {'name': 'Jenn', 'age': 23}
person_t = ('Jenn', 25)
person_l = ['Jenn', 26]

url = 'https://bgpstream.com/static/sessions.json'
r  = requests.get(url).json()

for i in r:
    #result = i.get('id', None)
    #if result == 107:
    if  i['id'] == 107 and i['status'] == '1':
        print(i)

sentance1 = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'

#works /w or w/o numberes
sentance2 = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])

sentance3 = 'My name is {name} and I am {age} years old.'.format(**person)

sentance4 = 'My name is {0} and I am {1} years old.'.format(*person_l)

print(sentance4)
