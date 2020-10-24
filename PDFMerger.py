import PyPDF2
import sys

inputs = sys.argv[1:] # Grabs all arguments excluding the first one


def pdfMerge(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write('Adrien Clay Resume Cover Letter.pdf')
pdfMerge(inputs)