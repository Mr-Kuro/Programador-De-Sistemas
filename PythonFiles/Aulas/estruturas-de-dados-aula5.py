tel = {'Icaro': 999641258, 'joao': 981765486}
tel['jose'] = 992346859
print(tel)
print(tel['joao'])
del tel['Icaro']

# print(tel)
# list(tel)
# sorted(tel)
# print(tel)

tel['Amanda'] = 981540226
print(tel)
print(sorted(tel))
print('Amanda' in tel)
print('Icaro' in tel)

print(tel.get('Amanda'))
tel.update({'Pedro': 999672834})
