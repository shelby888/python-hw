# • Ключ-значение :
#     ○ Написать программу, которая берет словарь и меняет местами ключи и значения.
#      Попытаться реализовать за наименьшее кол-во строк.
#         § Пример: {'key1': 'value1', 'key2': 'value2'} -> {'value1': 'key1', 'value2': 'key2'}

dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
reverce_dictionaty = dict()
print(dictionary)
for key in dictionary:
    reverce_dictionaty[dictionary[key]] = key
print(reverce_dictionaty)


