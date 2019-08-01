# • FizzBuzz:
#     ○ Написать программу, которая выводит на экран числа от 1 до 100.
#     При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
#      а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5,
#      то программа должна выводить слово «FizzBuzz».

for number in range(1, 101):
    printed_str = ''
    if (number % 3) == 0:
        printed_str = 'Fizz'
    if (number % 5) == 0:
        printed_str = printed_str + 'Buzz'
    if printed_str == '':
        print(number)
    else:
        print (printed_str)
