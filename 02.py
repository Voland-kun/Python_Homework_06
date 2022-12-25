#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def input_int():
    while True:
        try:
            user_number = input('Введите целое число: ')
            user_number = int(user_number)
            return user_number
        except ValueError:
            print('Введено не целое число.')

# def set_products(user_number):
#     result_list = []
#     product = 1
#     for i in range(1, user_number+1):
#         product *= i
#         result_list.append(product)
#     return result_list

# num = input_int()
# print(set_products(num))

num = input_int()
factorial = lambda i: 1 if i == 0 else i * factorial(i - 1)
product = [factorial(i+1) for i in range(num)]
print(product)