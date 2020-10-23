import pickle

with open("Options.pickle", "rb") as file:
    data = pickle.load(file)

options = data["options"]
score_options = data["score_options"]

print(options)


