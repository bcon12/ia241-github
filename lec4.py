'''
lec4
'''

my_tuple = 'a','b','c','d','e'
print(my_tuple)

my_2nd_tuple = ('a','b','c','d','e')
print(my_2nd_tuple)

not_a_tuple = 'a'
print(type(not_a_tuple))

is_a_tuple = ('a',)
print(is_a_tuple)

print(my_tuple[1])
print(my_tuple[1:3])
print(my_tuple[1:])
print(my_tuple[:3])
print(my_tuple[:])


my_car = {
    'color':'red',
    'maker':'toyato',
    'year':2015
}
print(my_car)
print(my_car['year'])
print(my_car['color'])

print(my_car.items())
print(my_car.keys())
print(my_car.values())
print(my_car.get('year'))

my_car['maker'] = 'Corolla'
my_car['year'] = 2020
print(my_car)
print(len(my_car))
print('color' in my_car)

'''
end lab4, the rest of this is me familiarizing myself with it
'''

test_ok = {
    'container':'red',
    'hull':4000,
    'box':'hybrid'
}
print(test_ok)
print(test_ok['box'])
print(test_ok['hull'])
print(len(test_ok))

print('container' in test_ok)

test_ok['hull'] = 'mixup'
print(test_ok)

print(test_ok.get('box'))


v1 = (1, 2, 3)
v2= [1, 1, 2, 2, 3, 4]

print(len(v1))

print (len(('this is a string').split()))