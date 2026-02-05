a = [1, 2, 3, 4]
b = [3, 4, 5]

union = set()

for x in a:
    union.add(x)

for x in b:
    union.add(x)

result = list(union)
print(sorted(result))
