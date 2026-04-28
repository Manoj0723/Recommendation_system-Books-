# Recommendation_system-
Recommendation  using python
#  Movie Recommendation System
 
A collaborative filtering-based movie recommendation system built with Python. It uses **cosine similarity** to find similar users and movies, enabling personalized movie recommendations based on user rating patterns.
 
---
 
##  Overview
 
This project implements two types of collaborative filtering:
 
- **User-User Filtering** – Finds users with similar taste and recommends movies they enjoyed
- **Item-Item Filtering** – Finds movies similar to ones a user has already rated highly
---
 
##  Dataset
 
The project expects two CSV files:
 
| File | Description |
|------|-------------|
| `movies.csv` | Contains `movieId`, `title`, `genres` |
| `ratings.csv` | Contains `userId`, `movieId`, `rating`, `timestamp` |
 
> Compatible with the [MovieLens dataset](https://grouplens.org/datasets/movielens/).
 
---
 
##  How It Works
 
1. **Load & Explore Data** – Reads `movies.csv` and `ratings.csv`, checks for duplicates and null values
2. **Merge DataFrames** – Joins movies and ratings on `movieId`
3. **Build User-Movie Matrix** – Creates a pivot table with users as rows and movie titles as columns
4. **Compute Cosine Similarity** – Calculates similarity scores between users (and between movies)
5. **Generate Recommendations** – Identifies the most similar users to a target user and surfaces their top-rated movies
---
 
##  Tech Stack
 
- **Python 3.x**
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Scikit-learn** – Cosine similarity computation
---
 
## Getting Started
 
### 1. Clone the repository
 
```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```
 
### 2. Install dependencies
 
```bash
pip install pandas numpy scikit-learn
```
 
### 3. Add the dataset
 
Place `movies.csv` and `ratings.csv` in the project root directory.
 
### 4. Run the notebook
 
Open `Recommendation.py` in Jupyter Notebook or convert and run it directly:
 
```bash
jupyter notebook Recommendation.py
```
 
---
 
##  Example Output
 
For **User ID 3**, the system finds the 3 most similar users and surfaces their top-rated movies as recommendations.
 
```
Most similar users to User 3: [313, 377, 532]
 
Top movies recommended:
 - Toy Story (1995)
 - Pulp Fiction (1994)
 - The Shawshank Redemption (1994)
```
 
---
 
##  Project Structure
 
```
movie-recommendation-system/
│
├── Recommendation.py    # Main recommendation logic (Jupyter Notebook)
├── movies.csv           # Movie metadata (not included – add your own)
├── ratings.csv          # User ratings (not included – add your own)
└── README.md
```
 
---
 
##  Future Improvements
 
- Add a content-based filtering approach using movie genres
- Build a simple web interface with Flask or Streamlit
- Incorporate matrix factorization (SVD) for better accuracy
- Handle cold-start problem for new users/movies
---
 
## 📄 License
 
This project is open-source and available under the [MIT License](LICENSE).
