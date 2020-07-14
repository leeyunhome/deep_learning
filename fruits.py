fruits = ['apple', 'apple', 'apple', 'banana', 'banana', 'kiwi', 'kiwi', 'strawberry', 'pineapple']

g = {}

for f in fruits:
    if f in g:
        g[f] = g[f] + 1
    else:
        g[f] = 1

print(type(g))
print(g)