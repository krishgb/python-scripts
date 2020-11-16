import os
import PyPDF2

files = os.listdir('./')

index = 0
for pdf in files:
    if pdf.endswith('.pdf'):
        files[index] = pdf
        print(f'{index+1}. {pdf}')
        index += 1

files = files[:index]

# pdf merger function
def pdf_merger():
    merger = PyPDF2.PdfFileMerger()
    for i in range(len(to_be_merged)):
        merger.append(files[int(to_be_merged[i]) - 1])
    print('\nSuccessfully Merged!')
    merger.write(input('\nPlease give a new name for your merged pdf: ') + '.pdf')
    print('\nAll done.')
try: 
    if len(files) > 1:
        to_be_merged = input('\nEnter the numbers of the pdf you want to merge\n').split(' ')
        pdf_merger() if len(to_be_merged) > 1 else print('Please Merge atleast two pdf files..')
except IndexError as err:
    print(err)