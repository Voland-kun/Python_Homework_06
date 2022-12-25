#Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

def input_int():
    while True:
        try:
            user_number = input('Введите целое число: ')
            user_number = int(user_number)
            return user_number
        except ValueError:
            print('Введено не целое число.')

# def dictionary_generation(user_number):
#     user_dictionary = {}
#     for i in range(1, user_number+1):
#         user_dictionary[i] = (1 + (1/i))**i
#     return user_dictionary

num = input_int()
# dictionary = dictionary_generation(num)
# print(dictionary)

dic = {i:(1 + (1/i))**i for i in range(1, num+1)}
print(dic)
print(sum(dic.values()))