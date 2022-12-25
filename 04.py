#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def input_int():
    while True:
        try:
            user_number = input('Введите целое число: ')
            user_number = int(user_number)
            return user_number
        except ValueError:
            print('Введено не целое число.')

# def fibonacci(user_number):
#     if user_number == 1 or user_number == 2:
#         return 1
#     elif user_number <= 0:
#         return fibonacci(user_number + 2) - fibonacci(user_number + 1)
#     else:
#         return fibonacci(user_number - 1) + fibonacci(user_number - 2)

num = input_int()
# lst = []

# for i in range(-num, num + 1):
#     lst.append(fibonacci(i))
# print(lst)

fib = lambda x: fib(x - 1) + fib(x - 2) if x > 2 else fib(x + 2) - fib(x + 1) if x < 1 else 1
result = [fib(i) for i in range(-num, num + 1)]
print(result)