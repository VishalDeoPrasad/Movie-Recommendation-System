import tkinter as tk
from tkinter import ttk
import pickle

movie = pickle.load(open("movie_list.pkl", "rb"))
movie_list = movie['title'].astype(str).tolist()

similarity = pickle.load(open("movie_similarity.pkl", "rb"))

def recommend(movie_name):
    index = movie[movie['title'] == movie_name].index[0]
    distance = list(enumerate(similarity[index]))
    distance = sorted(distance, key=lambda x:x[1], reverse=True)
    recommended_movie = []
    for i in distance[:10]:
        recommended_movie.append(movie.iloc[i[0]].title)
    return recommended_movie

def show_recommend():
    result_list.delete(0, tk.END)
    recommended = recommend(combo.get())
    for idx, movie in enumerate(recommended, start=1):
        # print(idx, movie)
        result_list.insert(tk.END, f"{idx}. {movie}")
    
root = tk.Tk()
root.geometry("500x450")
root.title("Movie Recommender System")

header = tk.Label(root, text="Movie Recommender System",
                  font=("Arial", 18, "bold"))
header.pack(pady=15)

tk.Label(root, text="Select Movie:",
         font=("Arial", 12)).pack(pady=5)

combo = ttk.Combobox(root, values=movie_list, width=50)
combo.pack()

btn = tk.Button(root, text="Show Recommend",
                font=("Arial", 12),
                bg="blue", fg="white",
                command=show_recommend)
btn.pack(pady=10)

tk.Label(root, text="Top 10 Recommended Movie",
         font=("Arial", 14, "bold")).pack(pady=10)

result_list = tk.Listbox(root, width=60, height=12)
result_list.pack(pady=5)
root.mainloop()