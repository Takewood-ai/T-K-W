import json

def train(text):
    words = text.split()

    model = {}

    for i in range(len(words)-1):
        word = words[i]
        next_word = words[i+1]

        if word not in model:
            model[word] = []

        model[word].append(next_word)

    return model


def save_model(model):
    with open("memory.json", "w", encoding="utf-8") as file:
        json.dump(model, file, ensure_ascii=False)


def load_model():
    try:
        with open("memory.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}
