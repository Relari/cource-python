
facebook = {'fundador': 'Mark Zuckerberg',
            'dominio': 'www.facebook.com'}

print(facebook['fundador'])
print(facebook['dominio'])

facebook_extra = {'usuarios': 2500}

facebook.update(facebook_extra)

print(facebook.keys())
print(facebook)

print(facebook.get('elemetos'))

