DATA_PATH = "/Users/CharlyZhang/Desktop/report"


dica = {"a":"1","b":"2"}

array = []
for k,v in dica.items():
    array.append("{k}:{v}".format(k=k,v=v))
    
print(array)

