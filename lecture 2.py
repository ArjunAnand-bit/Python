# str
stringVariable1 = 'Arjun' # 1st way to create string
stringVariable2 = str('Arjun') # 2nd way ro create string
print(stringVariable1, type(stringVariable1))
print(stringVariable2 , type(stringVariable2))

# int
intVariable1 = 3 # 1st way to create integer
intVariable2 = int(3)  # 2nd way to create integer
print(intVariable1, type(intVariable1))
print(intVariable2, type(intVariable2))

#float
floatVariable1 = 8.9
floatVariable2 = float(8.9)
print(type(floatVariable1))
print(type(floatVariable2))
 #complex
complexVariable1 = 7j
complexVariable2 = complex(7j)
print(type(complexVariable1))
print(type(complexVariable2))

#bool
boolVariable1 = False
boolVariable2 = bool(False)
print(type(boolVariable1))
print(type(boolVariable2))

#list
listVariable1 = [complexVariable1]
listVariable2 = list((complexVariable2, complexVariable1))
print(listVariable1, type(listVariable1))
print(listVariable2 ,type(listVariable2))


#tuple
tupleVariable1 = ('Arjun','Rishabh',5,True,0,5j)
tupleVariable2 = tuple(('Arjun','Rishabh',5,True, 0, 5j))
print (tupleVariable1)
print (tupleVariable2)