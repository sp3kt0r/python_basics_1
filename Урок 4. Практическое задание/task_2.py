"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""


result_list = []
list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list)

Введите список чисел: 300 2 12 44 1 1 4 10 7 1 78 123 55
Исходный список:  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
Список, элементы которого больше предыдущего:  [12, 44, 4, 10, 78, 123]

Process finished with exit code 0
