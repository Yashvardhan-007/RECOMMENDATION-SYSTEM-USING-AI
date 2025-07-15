import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv('movies.csv')

# Fill missing descriptions
df['description'] = df['description'].fillna('')

# Vectorize descriptions
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Calculate cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Mapping titles to index
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def get_recommendations(title, top_n=5):
    idx = indices.get(title)
    if idx is None:
        return "Movie not found."

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

if __name__ == "__main__":
    title = input("Enter a movie title: ")
    recommendations = get_recommendations(title)
    if isinstance(recommendations, str):
        print(recommendations)
    else:
        print("\nTop 5 recommendations:")
        for i, rec in enumerate(recommendations, start=1):
            print(f"{i}. {rec}")
