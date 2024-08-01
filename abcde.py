from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import unified_diff
import PyPDF2
import re
import numpy as np 

def extract_text_from_pdf(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            
            # Print the number of pages
            num_pages = len(pdf_reader.pages)
            print('Number of pages:', num_pages)
            
            # Extract text from the first page
            f_page = pdf_reader.pages[0]
            page_text = f_page.extract_text()
            
            return page_text
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def check_keywords_in_text(text, keywords):
    found_keywords = [word for word in keywords if word.lower() in text.lower()]
    return found_keywords

def find_numbers(text):
    # Find all numbers in the text
    numbers = re.findall(r'\d+', text)
    return numbers

# Path to the PDF file
pdf_path = ('invoice_77098_train.pdf', 'invoice_102857.pdf')

# Extract text from the PDF
extracted_text1 = extract_text_from_pdf('invoice_77098_train.pdf')
extracted_text2= extract_text_from_pdf('invoice_102857.pdf')

def compare_texts(text1, text2):
    text1_lines = text1.splitlines()
    text2_lines = text2.splitlines()
    
    diff = unified_diff(extracted_text1, extracted_text2, lineterm='')
    return '\n'.join(diff)

if extracted_text1 and extracted_text2:
    print("Extracted Text:")
    print(extracted_text1 , extracted_text2)
    
    # Keywords to check
    keywords = ['invoice', 'numbers', 'dates', 'amounts']
    
    # Check for keywords in the extracted text
    found_keywords1 = check_keywords_in_text(extracted_text1, keywords)
    found_keywords2 = check_keywords_in_text(extracted_text2, keywords)
    
    if found_keywords1:
        print("Found Keywords:", found_keywords1)
    else:
        print("Not Found")

    if found_keywords2:  
        print("found Keywords", found_keywords2)
    else: 
        print("not found")
    
    # Find and print all numbers in the text
    numbers1 = find_numbers(extracted_text1)
    print("Found Numbers:\n ", numbers1)
    
    numbers2 = find_numbers(extracted_text2)
    print("Found Numbers:\n ", numbers2)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([extracted_text1, extracted_text2])   

    similarity_matrix = cosine_similarity(tfidf_matrix)
    cosine_sim = similarity_matrix[0, 1]
    print("Cosine Similarity:", cosine_sim)



