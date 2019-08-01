# • Дубликаты:
#     ○ Написать программу, которая берет исходный список и формирует новый список.
#      В новом списке должны содержаться все элементы из исходного, за исключением дублей.
#         § Пример: [1, 1, 2, 3, 5,  4,5, 5, 6] -> [1, 2, 3, 5, 4, 6]

ls = [1, 1, 2, 3, 5,  4,5, 5, 6]
ls_non_duplicates = []
for element in ls:
    if element not in ls_non_duplicates:
        ls_non_duplicates.append(element)
print(ls_non_duplicates)