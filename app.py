import os
import PyPDF2
from flask import Flask, request, jsonify
import streamlit as st

app = Flask(__name__)

@app.route('/')
def home():
    st.title('Resume Search')

    uploaded_files = st.file_uploader("Upload PDF Files", accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            file.save(os.path.join("pdf_files", file.name))
        st.success("Files uploaded successfully!")

    return ""

@app.route('/search', methods=['POST'])
def search():
    skill = request.form.get('skill')
    results = []
    
    for filename in os.listdir("pdf_files"):
        if filename.endswith(".pdf"):
            with open(os.path.join("pdf_files", filename), 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                if skill.lower() in text.lower():
                    results.append(filename)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
