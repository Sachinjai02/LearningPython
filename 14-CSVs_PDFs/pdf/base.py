import PyPDF2
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
number_of_pages = len(pdf_reader.pages)
print(f"No of page pdf has {number_of_pages}")

for page_num in range(0, number_of_pages):
    page = pdf_reader.pages[page_num]
    page_text = page.extract_text()
    print(f"Page {page_num} contents are:\n{page_text}")

f.close()