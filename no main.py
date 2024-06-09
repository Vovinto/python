# Завдання
# Два списки цілих заповнюються випадковими числами.
# Сформуйте третій список, який містить:
# ■ елементи обох списків;
# ■ елементи обох списків без повторень;
# ■ елементи, спільні для двох списків;
# ■ тільки унікальні елементи кожного зі списків;
# ■ тільки мінімальне та максимальне значення кожного зі
# списків.
#
# import random
# lst_1 = [random.randint(0,10) for _ in range(10)]
# lst_2 = [random.randint(0,10) for _ in range(10)]
# print("перший лимт:",lst_1)
# print("другий лист:",lst_2)
#
# lst = lst_1+lst_2
# print("третій лист :",lst)
#
# lst = list (set(lst_1+lst_2))
# print("елементи обох списків без повторень:",lst)
#
# lst = set(lst_1) & set(lst_2)
# print("елементи, спільні для двох списків:",lst)

# lst = set(lst_1) ^ set(lst_2)
# lst4=[]
# for i in lst_1:
#     if lst_1.count(i) == 1:
#         lst4.append(i)
# for i in lst_2:
#     if lst_2.count(i) == 1:
#         lst4.append(i)
# print("тільки унікальні елементи кожного зі списків:",lst4)
#
# # тільки мінімальне та максимальне значення кожного зі
# # списків
#
# lst4 = []
# lst4.append(min(lst_1))
# lst4.append((max(lst_1)))
# lst4.append(min(lst_2))
# lst4.append(max(lst_2))
# print("тільки мінімальне та максимальне значення кожного зі списків",lst4)


# Завдання 1
# Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх елементів більше за нуль;
# якщо ні — тільки першу третину. Решту списку не сортуйте,
# а розташуйте у зворотному порядку

# import random
# num = 9
# lst = [random.randint(-100,100) for _ in range(num)]
# num = int(num / 3)
# lst_1 = 0
# lst4 = []
# count = []
# for i in lst:
#     lst_1 += i
# lst_1 = lst_1 / len(lst)
# if lst_1 > 0 :
#     for i in range(num*2):
#         lst4.append(max(lst))
#         if len(lst) != 1:
#             lst.remove(max(lst))
#     lst4 = lst4[::-1]
# else:
#     for i in range(num):
#         lst4.append(max(lst))
#         if len(lst) != 1:
#             lst.remove(max(lst))
    lst4 = lst4[::-1]
#     print(lst4)
print("Hello")


