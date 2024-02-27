import spacy
import os 
import nltk
import math
from nltk.tokenize import word_tokenize
from collections import Counter
import PyPDF2
import docx

nltk.download('punkt')
def my_cosine_similarity(skill_list1, skill_list2):

    # Preprocess and filter skills
    def preprocess_and_filter(skill_list):
        filtered_tokens = []
        for skill in skill_list:
            tokenized_word = word_tokenize(skill)
            for word in tokenized_word:
                cleaned_word = word.lower()
                if cleaned_word.isalnum():
                    filtered_tokens.append(cleaned_word)
        return Counter(filtered_tokens)

    # Create Vectors
    counter1 = preprocess_and_filter(skill_list1)
    counter2 = preprocess_and_filter(skill_list2)

    vector1 = [counter1[word] for word in counter1]
    vector2 = [counter2[word] for word in counter1]

    # Calculate Cosine Similarity
    dot_product = sum(i * j for i, j in zip(vector1, vector2))
    norm_vector1 = math.sqrt(sum(x ** 2 for x in vector1))
    norm_vector2 = math.sqrt(sum(x ** 2 for x in vector2))

    cosin_sim = dot_product / (norm_vector1 * norm_vector2) if (norm_vector1 * norm_vector2) != 0 else 0
    return cosin_sim



def read_text(file_path):
    file_extension = file_path.split('.')[-1].lower()
    if file_extension == 'docx':
        return read_docx(file_path)
    elif file_extension == 'pdf':
        return read_pdf(file_path)
    else:
        raise ValueError("Unsupported file type. Only DOCX and PDF files are supported.")

def read_docx(file_path):
    doc = docx.Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)
    
def read_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text