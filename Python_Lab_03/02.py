#2d Lists

xs = [3, 1, 2]
print(xs, xs[2])
print(xs[-1])
xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)
x = xs.pop()
print(x, xs)
nums = list(range(5))
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:2])
print(nums[:])
print(nums[:-1])
nums[2:4] = [8, 9]
print(nums[2:4])
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
for idx, animal in enumerate(animals):
    print(f'{idx + 1, animal}')   
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)
squares = [x ** 2 for i in nums]
print(squares)

enven_squares = [x ** 2 for x in nums if x % 2 == 0]
print(enven_squares)

#2e Dictionaries

d = {'cat': 'cute', 'dog':'furry'}
print(d['cat'])
print('cat' in d)
d['fish'] = 'wet'
print(d['fish'])
print(d.get('monkey', 'N/A'))
print(d.get('fish', 'N/A'))
del d['fish']
print(d.get('fish', 'N/A'))

for animal in d:
    legs = d[animal]
    print(f'{animal}, {legs}')
for animal, legs in d.items():
    print(f'{animal} , {legs}')    

nums = {0, 1, 2, 3, 4}
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)

#2f Sets

animals = {'cat', 'dog'}
print('cat' in animals)
print('fish' in animals)
animals.add('fish')
print('fish' in animals)
print(len(animals))
animals.add('cat')
print(len(animals))
animals.remove('cat')
print(len(animals))
for idx, animal in enumerate(animals):
    print(f'{idx + 1}, { animal}')


from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)

#2g Tuples

d = {(x, x + 1): x for x in range(10)}
t = (5, 6)
print(type(t))
print(d[t])
print(d[1, 2])