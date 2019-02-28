# my first program
print('Вашему вниманию, предлагается игра "кто хочет стать миллиардером"')

i = 0
while i < 2:
    question_1 = "Вопрос №1. Как называют футболиста обладающего плохой техникой?"
    print(question_1)
    variants_1 = ("слон", "дерево", "бомбардир", "кидала")
    correct_1 = variants_1[1]
    print(variants_1)
    answer_1 = input("введите ответ: ")

    if answer_1 == correct_1:
        print("Правильно!")
        i += 1
    else:
        print("Это фиаско братан!")
        break

    question_2 = "Вопрос №2. Что подбросила богиня раздора Эрида на пиршественный стол во время свадьбы Пелея и Фетиды?"
    print(question_2)
    variants_2 = ("граната", "венок", "наркотики", "яблоко")
    correct_2 = variants_2[3]
    print(variants_2)

    answer_2 = input("введите ответ: ")

    if answer_2 == variants_2[3]:
        print("Правильно!")
        i += 1
    else:
        print("Это фиаско братан!")
        break
else:
    print("Вы победили, ответив на все вопросы!")


