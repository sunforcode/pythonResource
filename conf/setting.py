DATA_PATH = "/Users/CharlyZhang/Desktop/report"


dica = {"a":"1","b":"2"}

array = []
for k,v in dica.items():
    array.append(k)
    array.append(dica[k])
print(array)