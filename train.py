from model import train, save_model

text = open("data.txt", "r", encoding="utf-8").read()

model = train(text)

save_model(model)

print("T-K-W обучился и сохранил память!")
