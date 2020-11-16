# page_remover.py is used to remove pages from a pdf

# To run this script you have to download PyPDF2 library
#       In Terminal run "pip3 install PyPDF2" 

# Run this script in terminal "python page_remover.py"

# The script prompts 3 input:
#       1st Prompt: The name of the pdf file to which the pages have to be removed.
#       2nd Prompt: Give a name to get the pdf with removed pages.
#       3rd Prompt: Enter the pages that have to be removed from the given pdf
#                   Example: 10 20
# Give space between the page numbers

from PyPDF2 import PdfFileReader, PdfFileWriter

file = input('Enter the pdf name without ".pdf" \n')
file = file + '.pdf'

output = input('Enter the pdf name you want to give to your modified pdf file without ".pdf" \n')
output = output + '.pdf'

pages_to_remove = input('Enter the pages to be removed: ')
pages_to_remove = pages_to_remove.split(' ')

for page in range(len(pages_to_remove)):
    pages_to_remove[page] = abs(int(pages_to_remove[page]))

given_pdf = PdfFileReader(file, 'r')
num_pages = given_pdf.numPages

if num_pages > 1:
    with open(output, 'wb') as new_file:
        writer = PdfFileWriter()
        for i in range(num_pages):
            if i+1 in pages_to_remove:
                continue
            else:
                p = given_pdf.getPage(i) 
                writer.addPage(p)
                writer.write(new_file)
                
        print('Removed Successfully!!')
else:
    print(f"\n Sorry! The pdf has {'no' if num_pages == 0 else 1} page.")