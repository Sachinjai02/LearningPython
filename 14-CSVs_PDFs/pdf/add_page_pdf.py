import PyPDF2
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfReader(f)

first_page = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(first_page)

pdf_output = open('Some_new_file.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()