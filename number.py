# Повторяшки из списка
mas1 = [1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 2, 6, 7, 8]
new_mas = []
for i in mas1:
    if mas1.count(i) > 1:
        new_mas.append(i)
new_mas1 = list(set(new_mas))
print(new_mas1)