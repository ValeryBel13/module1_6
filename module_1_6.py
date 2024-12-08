my_dict={'Denis': 1994, 'Victor':2000,'Andrey': 1989,'Victoria':1990}
print(my_dict)
print (my_dict.get('Victor'))
print (my_dict.get('Artem'))
my_dict.update({'Pavel':1999,
                'Oleg':1985})
print(my_dict)
#my_dict.pop('Victoria')
#print(my_dict)
a = my_dict.pop('Victoria')
print(my_dict)
print(a)
print(my_dict)

my_set_={1,2,3,4,4,4,5,4,6,7,3,3}
print(my_set_)
my_set_={1,2,3,(1,2,3),4,4,4,5,'Dog',4,6,7,3,3}
print(my_set_)
print(my_set_.discard(2))
print(my_set_)