# 📰 News Classification using Naive Bayes & BERT

## 📌 Overview

This project builds an NLP system to automatically classify news articles into four categories: World, Sports, Business, and Sci/Tech.
Two models were implemented and compared: a traditional machine learning model (Naive Bayes) and a transformer-based model (BERT).  
The final solution was deployed using Streamlit for real-time predictions.

---
## 🎯 Objectives

* Preprocess and clean textual data  
* Train and compare ML vs Deep Learning models  
* Evaluate performance using standard metrics  
* Deploy an interactive web application  

---
## 📊 Dataset

* News articles labeled into 4 categories:
  * World  
  * Sports  
  * Business  
  * Sci/Tech  

* Features:
  * Text (title + description)  

---
## ⚙️ Methodology

* Text preprocessing (cleaning, tokenization, lemmatization)  
* Feature extraction:
  * TF-IDF (Naive Bayes)  
  * Tokenization (BERT)  
* Train/test split (80/20)  
* Model training and evaluation  

---
## 🤖 Models

* **Multinomial Naive Bayes**  
  * Fast and efficient baseline  
  * Accuracy: ~87.7%  

* **BERT (Transformer)**  
  * Context-aware language model  
  * Accuracy: ~90.4%  

---
## 📈 Results

* BERT outperformed Naive Bayes across all metrics  
* Better handling of similar categories (e.g., Business vs World)  
* Naive Bayes remained fast and effective for simpler tasks  

---
## 🌐 Deployment

A Streamlit web app was built to:  
* Input custom news text  
* Predict category in real time  
* Display prediction with confidence score  

---
## 🖥 How to Use the Interface (Local Setup)

Follow these steps to run the interface locally:

1️⃣ Download/Clone the Project 
Ensure you have the folder containing:  
* `app.py` (Streamlit code)  
* `models/` folder (BERT or Naive Bayes saved model)  
* `requirements.txt` (Python dependencies)  

2️⃣ If using ZIP file  
* Extract the ZIP in your desired directory  
* Make sure the folder structure remains intact (`models/` + `app.py`)  

3️⃣ Install dependencies 
```bash
pip install -r requirements.txt

4️⃣ Run the Streamlit app
streamlit run app.py
This will open the interface in your browser at localhost:8501.

5️⃣ Use the interface
Enter any news text (headline or short paragraph)
Click Classify
See the predicted category and confidence percentage

---
## 🛠 Tools Used
Python
Scikit-learn
Hugging Face Transformers
PyTorch
NLTK
Streamlit

---
##💡 Key Insights  

Transformer models significantly improve text understanding
Traditional models still perform well with proper preprocessing
Deployment makes AI models accessible to non-technical users

---
## 🚀 Future Work

Use larger and multilingual datasets
Optimize model for faster inference (e.g., DistilBERT)
Improve deployment scalability

---
##📎 Notes
This is a team project demonstrates the full NLP pipeline from preprocessing to deployment.
