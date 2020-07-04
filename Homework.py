# list_1 = [
#         "https://allo.ua/ua/catalog/result/?q=phone",
#         "https://allo.ua/ua/naushniki/proizvoditel-beats",
#         "https://allo.ua/ua//catalog/proizvoditel-beats",
#         "https://allo.ua/ua/result/?q=samsung",
#         "https://allo.ua/ua/catalog/result/?q=lap",
#         "https://allo.ua/?q=samsung",
#          ]
# for v  in list_1 :
#     if "catalog" in v:
#         print(v)
# list_2 = [v for v in list_1  if "catalog" in v ]
# print(list_2)
# print("***********************************************************************")
# indexes = set((0, 2, 4, 6, 8, 10))
# chars = list('ненормульную')
# for i in indexes:
#    chars[i] = chars[i].upper()
# string = ''.join(chars)
# print(string)

# print("******************************")
# a3 = "строкакdd"
# i = len(a3) // 2
# for v in a3 :
#     if len(a3)%2 == 0 :
#      result = a3[i-1:i+1]
#     elif len(a3)%2 != 0 :
#      result = a3[i-1:i+2]
# print(result)
# print("*************************")
# text = 'серпстатфоревер'
# unique_letters = set(text)
# analize = {}
# for letter in unique_letters:
#     analize[letter] = text.count(letter)
# print(analize)
# print("*****************************")
# list5 = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# set2 = set(list5)
# print(set2)
# print("*******************************")
#4.1) убрать из него повторяющиеся элементы
list_of_numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1 , 1202 , 23123 ]
list_unique = list(set(list_of_numbers))
print(list_unique)
#4.2) вывести 3 наибольших числа из исходного массива
list_sort = sorted(list_unique)
list_big = [max(list_sort),max(list_sort[:-1]),max(list_sort[:-2])]
print(list_big)
#4.3) вывести индекс минимального элемента массива
index_list = list_sort.index(min(list_sort))
print(index_list)
# 4.4) вывести исходный массив в обратном порядке
list_opposite = list_of_numbers[::-1]
print(list_opposite)




























