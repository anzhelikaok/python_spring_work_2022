

a = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

sort_type = int(input('Введите тип сортировки:'))

age = int(input('Введите возраст'))

group = int(input('Введите группу'))

for key_login in a:
  print(key_login['login'])

keys_login = []
for d in a:

    keys_login.append(d['login'])

keys_age = []
for z in a:
    keys_age.append(z['age'])

keys_group = []
for n in a:
    keys_group.append(n['group'])
