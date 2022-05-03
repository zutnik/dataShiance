# my_list = []
# for number in range(0, 1000):
#     if number % 2 == 0:
#         my_list.append(number)
# print(my_list)
#
# my_list = [number for number in range(0, 1000) if number % 2 == 0]
# print(my_list)
#
#
# def times_tables():
#     lst = []
#     for i in range(10):
#         for j in range(10):
#             lst.append(i * j)
#     return lst
#
#
# times_tables() == [j * i for i in range(10) for j in range(10)]
#
# print(times_tables())
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [a + b + c + d for a in lowercase for b in lowercase for c in digits for d in digits]
print(answer)
# correct_answer == answer
