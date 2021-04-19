lista = [5, 3, 4, 5, 9]

pprint(str.join('---', map(lambda x: str(x), filter(lambda x: x > 5 and x < 9, lista))))
