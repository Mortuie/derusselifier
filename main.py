from PyPDF2 import PdfFileReader, PdfFileWriter
import sys, os


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
    # try:
    #     source, destination = sys.argv[1], sys.argv[2]
    # except:
    #     print("Not enough cli args passed in. Need at least 2 for source and destination paths.")
    #     exit(1)
    # remove_slides(source, destination)