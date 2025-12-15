# 🎬 Movie Recommender System (Machine Learning)

## 📌 Project Overview
This project is a **content-based Movie Recommender System** built using machine learning techniques and extensive data cleaning. The system analyzes movie metadata and recommends similar movies based on **cosine similarity**, ensuring relevant and personalized suggestions. The project demonstrates strong skills in data preprocessing, feature engineering, and similarity-based recommendation algorithms.

---

## 🧠 How It Works
1. Raw movie data is cleaned, processed, and standardized  
2. Important features (such as genres, keywords, overview, cast, and crew) are combined  
3. Text data is vectorized using **TF-IDF / Count Vectorizer**  
4. **Cosine similarity** is calculated between movies  
5. Based on the selected movie, the system recommends the most similar movies  

---

## 📸 Application Preview
![Movie Recommender System](img-2.png)

---

## 🧹 Data Cleaning & Preprocessing
- Removed null and duplicate records  
- Standardized movie titles and text features  
- Processed textual columns (genres, overview, keywords)  
- Feature extraction and transformation for ML modeling  
- Created similarity matrix for recommendations  

---

## 🤖 Machine Learning Technique
- **Model Type:** Content-Based Recommendation System  
- **Algorithm:** Cosine Similarity  
- **Vectorization:** TF-IDF / Count Vectorizer  
- **Similarity Metric:** Cosine Distance  

---

## 🧰 Tools & Technologies
- Python  
- Pandas & NumPy  
- Scikit-learn  
- Streamlit  
- Natural Language Processing (NLP)  
- Machine Learning  

---

## 📂 Dataset Information
- Source: Public Movie Dataset  
- Format: CSV  
- Records: 10,000+ movies  
- Features: Title, Genres, Overview, Keywords, Cast, Crew  

---

## ▶️ How to Run the Project
1. Clone the repository  
```bash
git clone https://github.com/your-username/movie-recommender-system.git
