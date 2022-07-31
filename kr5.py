# кратные 5 в диопозоне от 1 до 500
mas = []
for i in range(1, 500 + 1, 1):
    if i % 5 == 0:
        mas.append(i)
print(mas)
