color_1 = input("Введите 1ый цвет: ").lower()
color_2 = input("Введите 2ой цвет: ").lower()


match (color_1, color_2):
     case ("красный", "синий") | ("синий", "красный"):
        print("Фиолетовый")
     case ("синий", "желтый") | ("желтый", "синий"):
        print("Зеленый")
     case ("красный", "желтый") | ("желтый", "красный"):
        print("Оранжевый")
     case _:
        print("Введены неверные цвета")



# с помощью if:

# color_1 = input("Введите 1ый цвет: ").lower()
# color_2 = input("Введите 2ой цвет: ").lower()
# valid_colors = ["красный", "синий", "желтый"]
# if color_1 not in valid_colors or color_2 not in valid_colors:
#    print("Введены неверные цвета")
# elif color_1 == color_2:
#    print("Введены одинаковые цвета")
# else:
#     pair = {color_1, color_2}
#     if pair == {"красный", "синий"}:
#         print("Фиолетовый")
#     elif pair == {"красный", "желтый"}:
#         print("Оранжевый")
#     elif pair == {"синий", "желтый"}:
#         print("Зеленый")