import random
from model import load_model

# Загружаем память T-K-W
model = load_model()

if not model:
    print("Память пуста! Сначала запусти обучение.")
    exit()

def generate(start_word, length=10):
    result = [start_word]
    word = start_word

    for _ in range(length):
        if word in model:
            word = random.choice(model[word])
            result.append(word)
        else:
            break

    return " ".join(result)


print("T-K-W 0.2 запущен!")
print("Память загружена.")
print("Напиши 'выход' для остановки.")

while True:
    user = input("Ты: ")

    if user.lower() == "выход":
        print("T-K-W: До встречи!")
        break

    words = user.split()

    if words[0] in model:
        print("T-K-W:", generate(words[0]))
    else:
        print("T-K-W: Я пока не знаю это слово.")
