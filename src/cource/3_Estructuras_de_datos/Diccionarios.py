
facebook = {'fundador': 'Mark Zuckerberg',
            'dominio': 'www.facebook.com'}

print(facebook['fundador'])
print(facebook['dominio'])

facebook['dominio'] = 'https://www.facebook.com'
print(facebook['dominio'])

facebook_extra = {'usuarios': 2500}

facebook.update(facebook_extra)

print(facebook.keys())
print(facebook.values())

print(facebook)

print(facebook.get('elemetos'))

exit(0)