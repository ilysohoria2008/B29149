result = []
def divider(a, b):
 if a < b:
     raise ValueError('Problem')
 if b > 100:
     raise IndexError('Problem')
 return a/b
data = {10: 2, 2: 5, 4: 18, 0, 15, 8,  4}
for key in data:
 result = divider(key, data[key])
 result.append(result)

print(result)