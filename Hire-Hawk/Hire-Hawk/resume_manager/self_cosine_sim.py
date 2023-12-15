import nltk
from nltk.tokenize import word_tokenize
import numpy as np
import math
import PyPDF2
import docx

nltk.download('punkt')

def my_cosine_similarity(resume1, resume2):
    tokens1 = word_tokenize(resume1)
    tokens2 = word_tokenize(resume2)

    casual_words = {'can', 'will', 'yourselves', 'don', 'them', 'where', "hadn't", "aren't", 'its', 'here', "doesn't", 'been', 'on', 'was', 'up', 'needn', 'off', 'most', 'other', 'the', 'there', 've', 'himself', 'a', 'all', 'won', 'only', 'but', 'or', 'my', 'those', 'now', 'shouldn', 'both', 'isn', "she's", 'mustn', 'an', 'be', 'if', 'do', 'than', 'they', 'nor', 'how', 'y', "should've", 'for', 'theirs', 'under', "don't", 'should', 'herself', 'him', 'that', 'his', 'i', 't', 'll', 'not', 'mightn', "isn't", 'had', "you'd", 'your', 'why', "wouldn't", 'myself', 'we', 'again', 'out', 'to', "haven't", 'her', 'our', 'he', 'few', "hasn't", 'after', "it's", "didn't", 'does', 'because', 'from', "wasn't", "you've", 'more', 'is', 'd', 'have', 'above', 'ma', 'having', 'at', 'before', 'as', "that'll", "you're", 'with', 'no', 'over', 're', 'of', 'and', 'while', 'own', 'which', 'being', 'ourselves', 'you', 'themselves', 'am', 'this', 'o', 'haven', 'during', "you'll", 'doing', 'me', 'each', 'then', 'wasn', 'who', 'she', 'yourself', 'between', 'in', 'what', 'very', "mightn't", 'itself', 'such', 'same', 'their', 'down', 'm', 'below', 'further', 'doesn', "weren't", "couldn't", 'these', 'hadn', 'about', 'hers', 'didn', 'couldn', 'through', 'aren', 'ours', 'it', 'whom', 'just', 'too', "mustn't", 'weren', "won't", "shan't", 'hasn', 'once', 'are', 'has', 'against', 'any', 'when', "needn't", 'by', 'yours', 'some', 'so', 'wouldn', "shouldn't", 's', 'were', 'did', 'until', 'ain', 'into', 'shan'}
    
    filtered_tokens1 = []
    for word in tokens1:
        if word.isalnum() and word.lower() not in casual_words:
            filtered_tokens1.append(word.lower())
            
    filtered_tokens2= []
    for word in tokens2:
        if word.isalnum() and word.lower() not in casual_words:
            filtered_tokens2.append(word.lower())
            

    unique_words = set(filtered_tokens1 + filtered_tokens2)
   
    vector1 = []
    for word in unique_words:
        count = filtered_tokens1.count(word)
        vector1.append(count)
    vector2 = []
    for word in unique_words:
        count = filtered_tokens2.count(word)
        vector2.append(count)
    
    def dot_product(vector1,vector2):
        sum=0
        for i,j in zip(vector1,vector2):
            sum = sum+(i*j)
        return sum
    
    def magnitude(vector):
        sum =0
        for x in vector: 
            sum = sum+x**2
        square_root = math.sqrt(sum)
        return square_root
    
    dot_product = dot_product(vector1,vector2)
    norm_vector1= magnitude(vector1)
    norm_vector2 = magnitude(vector2)
    cosin_sim = dot_product / (norm_vector1 * norm_vector2)
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