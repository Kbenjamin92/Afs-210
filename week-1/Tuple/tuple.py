from collections import defaultdict

classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

dictionary = defaultdict(list)

for class_name, roll_id in classes:
    dictionary[class_name].append(roll_id)

print(dictionary)