import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import matplotlib.pyplot as plt

# Load model and tokenizer
model_path = "models"  # folder that contains your saved model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Move to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

st.title("📰 News Category Classifier")
st.write("Enter a news text below to see which category it belongs to:")

# Text input
user_input = st.text_area("Write your news text here:")

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Tokenize input
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        # Get predictions
        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

        # Define labels
        labels = ["World", "Sport", "Business", "Sci/Tech"]
        pred_idx = torch.argmax(probs, dim=1).item()
        confidence = probs[0][pred_idx].item()

        st.success(f"Predicted Category: **{labels[pred_idx]}** (Confidence: {confidence:.2f})")

        # Convert to numpy for plotting
        probs_np = probs[0].cpu().numpy()

        # Plot as bar chart (dark blue)
        fig, ax = plt.subplots()
        ax.bar(labels, probs_np, color="#003366")
        ax.set_ylabel("Probability")
        ax.set_title("Prediction Confidence per Category")
        ax.set_ylim(0, 1)
        st.pyplot(fig)
