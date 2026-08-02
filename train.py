text = open("data.txt", "r", encoding="utf-8").read()

words = text.split()

model = {}

for i in range(len(words)-1):
    word = words[i]
    next_word = words[i+1]

    if word not in model:
        model[word] = []

    model[word].append(next_word)

print("T-K-W обучен!")
print(model)
