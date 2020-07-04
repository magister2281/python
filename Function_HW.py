##Задание номер 1
pass_letters = list()
pass_numbers = list()
exeption_alpha_num = ["Доступны только буквы или цифры"]
exeption_len_letters = ["Нечётное количество букв"]
exeption_len_num = ["Чётное количество цифр"]
def validate_password(password):
  for value in password :
       if value.isnumeric():
        pass_numbers.append(value)
       if value.isalpha():
           pass_letters.append(value)
  for value in password:
    if not (value.isalpha() or value.isnumeric()):
        return print(exeption_alpha_num)
  for value in pass_letters,pass_numbers:
    if   len(pass_letters) % 2 != 0 :
        return print(exeption_len_letters)
    if  len(pass_numbers) > 0  and len(pass_numbers) % 2 != 1 :
         return print(exeption_len_num)
#
validate_password('22344')
##Задание номер 2 с доп заданием( доп задание вышло не очень как по мне в плане гибкости)
# list_number = []
# def int_converter(number):
#  print(number)
#  bin_number = bin(number)
#  print(bin_number[2:])
#  oct_number = oct(number)
#  print(oct_number[2:])
#  hex_number = hex(number)
#  print(hex_number[2:])
#  list_numbers = [number,oct_number[2:],bin_number[2:], hex_number[2:]]
#  for value in list_numbers:
#      list_number.append(value)
# int_converter(230)
# def print_table(data):
#   for i in range(len(data)):
#     data_list = data[1]
#     dash = '-' * 49
#     if i == 0:
#       print(dash)
#       print('| {:<6s} | {:>8s} | {:>8s} | {:>13s} |'.format(data[i][0],data[i][1],data[i][2],data[i][3]))
#       print('| {:<7s} | {:>8s} | {:>8s} | {:>13s} |'.format(str(data_list[0]),str(data_list[1]),
#                                                             str(data_list[2]),str(data_list[3])))
#       print(dash)
# print_table([["Decimal", "Octal", "Binary", "Hexadecimal"],list_number])






