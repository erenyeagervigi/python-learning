a_values = [1,2,3,4,5]
b_values = [2,3,5,6,7]

values = []
for i in a_values:
    if i not in b_values:
        values.append(i)

print(values)
