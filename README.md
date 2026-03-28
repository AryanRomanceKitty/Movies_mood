🎬 Movie Mood Recommender
📌 About
This project is a simple movie recommendation system that suggests movies based on the user’s mood.
The main idea is pretty basic — if someone is feeling happy, sad, or excited, the system tries to recommend movies that match that feeling.
Instead of using any big or complex dataset, I created a small dataset on my own and built everything from scratch. The goal was to understand how recommendation systems actually work at a basic level.

⚙️ How It Works
•	First, the movie description and mood are combined into one text
•	Then, this text is converted into numbers using word frequency
•	After that, cosine similarity is used to compare different movies
•	Based on the similarity score, the system recommends the top 5 movies

🛠️ Tools Used
•	Python
•	pandas
•	NumPy
•	SciPy

📂 Files in the Project
•	create_dataset.py → used to generate the dataset
•	movies_mood.csv → the dataset file
•	main.py → main code for recommendations

▶️ How to Run
1.	First, create the dataset:
python create_dataset.py
2.	Then run the main program:
python main.py
3.	Enter your mood when asked (like happy, sad, excited)

💡 Example
If you enter:
happy
You might get something like:
Hangover  
3 Idiots  
Deadpool  

🎯 What I Learned
While making this project, I understood:
•	how to handle data using pandas
•	how text can be converted into numbers
•	how similarity between data can be calculated
•	how a basic recommendation system works

🚀 Future Improvements
•	Add more movies to improve accuracy
•	Include more moods
•	Make a simple UI instead of terminal

 Final Thoughts
This project is simple but helped me understand the basics of AI/ML concepts like text processing and similarity. It’s not very advanced, but it’s a good starting point for building more complex systems later.
