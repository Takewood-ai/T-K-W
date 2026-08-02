import random

# Загружаем обученную модель
text = open("data.txt", "r", encoding="utf-8").read()

words = text.split()

model = {}

for i in range(len(words)-1):
    word = words[i]
    next_word = words[i+1]

    if word not in model:
        model[word] = []

    model[word].append(next_word)


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


print("T-K-W 0.1 запущен!")
print("Напиши 'выход' для остановки.")

while True:
    user = input("Ты: ")

    if user == "выход":
        break

    first_word = user.split()[0]

    if first_word in model:
        answer = generate(first_word)
        print("T-K-W:", answer)
    else:
        print("T-K-W: Я пока не знаю это слово.")
