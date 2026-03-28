import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
from collections import Counter

movies = pd.read_csv("movies_mood.csv")

movies["tags"] = (movies["description"] + " " + movies["mood"]).str.lower()

all_words = []
for text in movies["tags"]:
    all_words.extend(text.split())

common_words = [word for word, _ in Counter(all_words).most_common(100)]


def text_to_vector(text):
    words = text.split()
    return np.array([words.count(word) for word in common_words])


vectors = [text_to_vector(text) for text in movies["tags"]]


def similarity(v1, v2):
    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        return 0
    return 1 - cosine(v1, v2)


def recommend(user_mood):
    user_vec = text_to_vector(user_mood.lower())

    scores = []
    for i, vec in enumerate(vectors):
        scores.append((i, similarity(user_vec, vec)))

    top = sorted(scores, key=lambda x: x[1], reverse=True)[:5]

    print("\n" + "=" * 40)
    print("  MOVIE RECOMMENDATIONS")
    print("=" * 40 + "\n")

    for i, (index, score) in enumerate(top, start=1):
        title = movies.iloc[index].title
        print(f"{i}. {title}  ⭐ ({score:.2f})")

    print("\n" + "=" * 40 + "\n")


# UI feel
print("=" * 40)
print("🎥 Welcome to Movie Mood Recommender")
print("=" * 40)

mood = input("\nEnter your mood (happy/sad/excited): ")

recommend(mood)
