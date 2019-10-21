from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import sys, os

def merge(files, destination):
    merged = PdfFileMerger()

    for file in files:
        with open(file, 'rb') as f:
            pdf = PdfFileReader(f)

            if pdf.isEncrypted:
                pdf.decrypt('')

            merged.append(pdf)

    with open(destination, 'wb') as output:
        merged.write(output)

def merge_multiple_files(files, destination):
    unique_pdf = PdfFileWriter()

    for file in files:
        print("Trying to add this file: " + file + "!")
        with open(file, 'rb') as f:
            pdf = PdfFileReader(f)
            if pdf.isEncrypted:
                pdf.decrypt('')
            number_of_pages = pdf.getNumPages()

            for page in range(0, number_of_pages):
                pdfpage = pdf.getPage(page)
                print(pdfpage.extractText())
                unique_pdf.addPage(pdfpage)

    for page in range(unique_pdf.getNumPages()):
        print(unique_pdf.getPage(page).extractText())
    return unique_pdf

def remove_slides(source, destination):
    number_of_pages = 0
    unique_pages = []

    unique_pdf = PdfFileWriter()

    with open(source, 'rb') as f:
        pdf = PdfFileReader(f)
        if pdf.isEncrypted:
            pdf.decrypt('')
        number_of_pages = pdf.getNumPages()

        for pages in range(0, number_of_pages):
            curr_page = ''.join(pdf.getPage(pages).extractText().split()[:-1])
            if pages == number_of_pages - 1:
                unique_pdf.addPage(pdf.getPage(pages))
                continue
            next_page = ''.join(pdf.getPage(pages + 1).extractText().split()[:-1])

            if curr_page in next_page:
                continue
            else:
                unique_pdf.addPage(pdf.getPage(pages))


        with open(destination, "wb") as output:
            unique_pdf.write(output)

if __name__ == '__main__':
    z = list(filter(lambda x: x.startswith("slides"), os.listdir()))
    z.sort()
    print(z)
    merge(z, 'test_merge.pdf')
    # try:
    #     source, destination = sys.argv[1], sys.argv[2]
    # except:
    #     print("Not enough cli args passed in. Need at least 2 for source and destination paths.")
    #     exit(1)
    # remove_slides(source, destination)