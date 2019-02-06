import pandas

file = 'Geka.xlsx'
xl = pandas.ExcelFile(file)
df = xl.parse('Sheet1')

name = df[3].tolist()
city = df[4].tolist()
address = df[5].tolist()
f = lambda x, y : str(x) + ' ' + str(y)
geo = map(f,city, address)

data = [list(i) for i in zip(name, geo)]

#return list of lists
