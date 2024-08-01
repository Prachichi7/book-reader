Document Similarity Matching with Python
This project implements a system to compare and match invoices based on their content and structure. It utilizes techniques like text extraction, keyword identification, and cosine similarity to identify the most similar invoice to a new one within a database.

Functionality Overview:
Text Extraction: The system extracts text content from PDF invoices using the PyPDF2 library.

Feature Extraction:
Keywords: It identifies relevant keywords like "Invoice", "Total", "Date", etc., using regular expressions.
Numbers: It extracts numerical values from the text using regular expressions (optional).
Cosine Similarity: It utilizes the sklearn.metrics.pairwise.cosine_similarity function from Scikit-learn to calculate the cosine similarity between the feature vectors of two invoices. Text is pre-processed using TF-IDF (Term Frequency-Inverse Document Frequency) to create these feature vectors.
Matching: The system compares the cosine similarity scores of the new invoice with all invoices in the database and identifies the one with the highest score as the most similar match.

Note: This is a basic implementation, and more advanced techniques can be explored for better accuracy.

Dependencies
Python 3.x
NumPy
PyPDF2
re (regular expressions)
scikit-learn

Installation:
cmd
pip install numpy PyPDF2 scikit-learn


Running the Code
Download the code and the provided invoice data (Do not upload data online!).
Ensure you have the required libraries installed using pip install.
Update the pdf_path variable in the code to point to the location of your invoice PDFs.
Run the script using python your_script.py.

1. Place your PDF files in the same directory as the script.
2. Update the `pdf_path` variable with the paths of your PDF files.
3. Run the script to extract text, find keywords and numbers, and calculate the cosine similarity between the invoices.

## Script Details

### `extract_text_from_pdf(pdf_path)`

Extracts text from the first page of the given PDF file.

### `check_keywords_in_text(text, keywords)`

Checks for the presence of specified keywords in the extracted text.

### `find_numbers(text)`

Finds all numbers in the extracted text.

### `compare_texts(text1, text2)`

Compares two texts line by line and returns the differences.

### `main`

The main function extracts text from the PDFs, checks for keywords, finds numbers, and calculates the cosine similarity between the invoices.

## Running the Script

Run the script using Python:

```bash
python abcd.py

Output
The script will output:

Extracted text from each PDF
Found keywords
Found numbers
Cosine similarity score between the invoices
The script displays the extracted text from the sample invoices, identified keywords (if any), extracted numbers (if enabled), and the cosine similarity score between the two invoices.
