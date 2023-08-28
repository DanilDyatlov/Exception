#TASK1
# class InvalidNumberException(Exception):
#     pass

# def positive_numbers(number):
#     if number <= 0:
#         raise InvalidNumberException("Некорректное число")
#     else:
#         print("Число корректно")

# number = int(input("Введите число: "))
# positive_numbers(number)

#TASK2
# class  DivisionByZeroException(Exception):
#     pass

# def divesion_numbers(num1, num2):
#     if num2 == 0:
#         raise DivisionByZeroException("Деление на ноль недопустимо")
#     else:
#         result = num1/num2
#         print(f'Резудьтат деления: {result}')  

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# divesion_numbers(num1, num2)

#TASK3
# class  NumberOutOfRangeException(Exception):
#     pass
# class  NumberOutOfRangeException(Exception):
#     pass
# class  NumberSumException(Exception):
#     pass
# class  DivisionByZeroException(Exception):
#     pass

# def checked(num1, num2, num3):
#     sum = num1 + num2
#     if num1 > 100:
#         raise NumberOutOfRangeException("Первое число вне допустимого диапазона")
#     if num2 < 0:
#         raise NumberOutOfRangeException("Второе число вне допустимого диапазона")
#     if sum < 10:
#         raise DivisionByZeroException("Сумма первого и второго чисел слишком мала")
#     if num3 == 0:
#         raise DivisionByZeroException("Деление на ноль недопустимо")
#     else:
#        print('Проверка пройдена успешно') 

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# checked(num1, num2, num3)