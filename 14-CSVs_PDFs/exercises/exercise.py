import csv
import PyPDF2
import re

data = open('find_the_link.csv', encoding='utf-8')

csv_data = csv.reader(data)

# reformat csv_data into list of lists python object
data_lines = list(csv_data)

rows = len(data_lines)
cols = len(data_lines[0])

path = ""
for diag in range(min(rows, cols)):
    path = path + data_lines[diag][diag]

print(path)

file = open('Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfReader(file)
num_pages = len(pdf_reader.pages)
phone = ""
for page_num in range(num_pages):
    pdf_text = pdf_reader.pages[page_num].extract_text()
    print(pdf_text)
    pattern = re.compile(r'(\d{3}).(\d{3}).(\d{4})')
    phone = re.search(pattern, pdf_text)
    if phone:
        break

print(phone.group())

