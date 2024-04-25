# from PyPDF2 import PdfFileWriter, PdfFileReader
#
#
# def secure_pdf(file, password):
#     parser = PdfFileWriter(file)
#     pdf = PdfFileReader(file)
#     for page in range(pdf.getNumPages()):
#         parser.addPage(pdf.getPage(page))
#     parser.encrypt(password)
#     with open(f"encrypted_{file}", "wb") as f:
#         parser.write(f)
#         f.close()
#     print(f"encrypted_{file} Created...")
#
#
# if __name__ == "__main__":
#     file = "pdf_file_1.pdf"
#     password = "12345678"
#     secure_pdf(file, password)
#
