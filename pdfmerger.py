import os
import PyPDF2
# import glob
from os import listdir
from os.path import isfile, join
mypath = os.getcwd()+'\pdfsToBeMerged'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# keep this outside loop so that it will hold all the tobe merged files
output = PyPDF2.PdfFileMerger()
for file in onlyfiles:
    if file.endswith('.pdf'):
        # The os.listdir() function will return names relative to the directory you're listing then.
        # You need to reconstruct the absolute path to open those files.
        absfile = os.path.join(mypath, file)
        pdf_file = PyPDF2.PdfFileReader(open(absfile, 'rb'))
        output.append(pdf_file)

with open("merged.pdf", "wb") as output_stream:
    output.write(output_stream)
