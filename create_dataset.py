import pandas as pd

data = [
    ["Avengers", "action hero save world fight battle", "excited"],
    ["Titanic", "love emotional ship tragedy romance", "sad"],
    ["Hangover", "comedy fun friends party", "happy"],
    ["Joker", "dark mental crime emotional", "sad"],
    ["Fast & Furious", "cars racing action thrill", "excited"],
    ["3 Idiots", "college fun emotional life lessons", "happy"],
    ["Interstellar", "space science emotional journey", "thoughtful"],
    ["Deadpool", "action comedy funny hero", "happy"],
    ["Batman", "dark hero action crime", "excited"],
    ["Notebook", "love emotional romance", "sad"],
]

df = pd.DataFrame(data, columns=["title", "description", "mood"])
df.to_csv("movies_mood.csv", index=False)

print("Dataset created!")
