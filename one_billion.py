# my first program
print('Вашему вниманию, предлагается игра "кто хочет стать миллиардером"')

question_1 = "как называют футболиста обладающего плохой техникой?"
print(question_1)
variants_1 = ("слон", "дерево", "бомбардир", "кидала")
print(variants_1)
answer_1 = input("введите ответ: ")

if answer_1 == "дерево":
    print("Правильно!")
else:
    print("Попробуйте еще раз")

print("Переходим к вопросу номер 2")

question_2 = "Что подбросила богиня раздора Эрида на пиршественный стол во время свадьбы Пелея и Фетиды?"
print(question_2)
variants_2 = ("граната", "венок", "наркотики", "яблоко")
print(variants_2)

answer_2 = input("введите ответ: ")

if answer_2 == "яблоко":
    print("Правильно!")
else:
    print("Попробуйте еще раз")
