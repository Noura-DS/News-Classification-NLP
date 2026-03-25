# 📰 News Classification using Naive Bayes & BERT

## 📌 Overview
This project builds an NLP system to automatically classify news articles into four categories: **World, Sports, Business, and Sci/Tech**. Two models were implemented and compared: a traditional machine learning model (**Naive Bayes**) and a transformer-based model (**BERT**). The final solution was deployed using **Streamlit** for real-time predictions.

## 🎯 Objectives
- Preprocess and clean textual data  
- Train and compare ML vs Deep Learning models  
- Evaluate performance using standard metrics  
- Deploy an interactive web application  

## 📊 Dataset
**Categories:** World, Sports, Business, Sci/Tech  
**Features:** Text (title + description)  

## ⚙️ Methodology
- Text preprocessing: cleaning, tokenization, lemmatization  
- Feature extraction: TF-IDF (Naive Bayes) & Tokenization (BERT)  
- Train/test split: 80/20  
- Model training and evaluation  

## 🤖 Models
**Multinomial Naive Bayes** – Fast and efficient baseline, Accuracy: ~87.7%  
**BERT (Transformer)** – Context-aware language model, Accuracy: ~90.4%  

## 📈 Results
- BERT outperformed Naive Bayes across all metrics  
- Better handling of similar categories (e.g., Business vs World)  
- Naive Bayes remained fast and effective for simpler tasks  

## 🌐 Deployment
A Streamlit web app was built to:  
- Input custom news text  
- Predict category in real time  
- Display prediction with confidence score  

## 🖥 How to Use the Interface (Local Setup)
1️⃣ **Download/Clone the Project** – Ensure you have `app.py`, `models/` folder, and `requirements.txt`  
2️⃣ **If using ZIP file** – Extract ZIP and keep folder structure intact  
3️⃣ **Install dependencies** – `pip install -r requirements.txt`  
4️⃣ **Run the Streamlit app** – `streamlit run app.py` (opens at localhost:8501)  
5️⃣ **Use the interface** – Enter news text, click **Classify**, see predicted category and confidence  

## 🛠 Tools Used
Python, Scikit-learn, Hugging Face Transformers, PyTorch, NLTK, Streamlit  

## 💡 Key Insights
- Transformer models significantly improve text understanding  
- Traditional models still perform well with proper preprocessing  
- Deployment makes AI models accessible to non-technical users  

## 🚀 Future Work
- Use larger and multilingual datasets  
- Optimize model for faster inference (e.g., DistilBERT)  
- Improve deployment scalability  

## 📎 Notes
This team project demonstrates the full NLP pipeline from preprocessing to deployment.
