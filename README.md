# RECOMMENDATION-SYSTEM-USING-AI

# 🎯 Simple Recommendation System

A Python-based recommendation system that suggests items (e.g., movies) to users based on their preferences using **content-based filtering**. This project helps beginners understand the core principles of recommendation systems using real datasets.

## 🚀 Features

- Recommends similar movies based on a given title
- Uses content-based filtering with cosine similarity
- Easy-to-understand, beginner-friendly code
- Ready to plug in with other types of data (books, products, etc.)

## 📁 Dataset

The project uses a CSV file (`movies.csv`) with columns like:
- `title`
- `genres`
- `description` (or `overview`)

You can replace the dataset with your own.

## ⚙️ Algorithms Used

### ✅ Content-Based Filtering

- Vectorizes movie descriptions using TF-IDF
- Calculates similarity using cosine similarity
- Recommends items similar to the one the user liked

You can upgrade it to include:
- **Collaborative Filtering**
- **Hybrid Filtering**

## 📥 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/recommendation-system.git
   cd recommendation-system
