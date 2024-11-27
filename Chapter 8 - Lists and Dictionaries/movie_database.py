table = {'1975': 'Holy Grail',
         '1979': 'Life of Brian',
         '1983': 'The Meaning of Life'}

year = '1983'
movie = table[year]
print(movie)

for year in table:
    print(year + '\t' + table[year])

table = {'Holy Grail': '1975',
         'Lif of Brian': '1979',
         'The Meaning of Life': '1983'}

print(table['Holy Grail'])

print(list(table.items()))

print([title for (title, year) in table.items() if year == '1975'])

k = 'Holy Grail'
print(table[k])

v = '1975'
print([key for (key, value) in table.items() if value == v])
print([key for key in table.keys() if table[key] == v])

table = {1975: 'Holy Grail',
         1979: 'Life of Brian',
         1983: 'The Meaning of Life'}

print(table[1975])
print(list(table.items()))
