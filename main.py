from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os, sys

def merge_files(destination_path, files):
    merged_file = PdfFileMerger()

    for file in files:
        with open(file, 'rb') as f:
            pdf = PdfFileReader(f)

            if pdf.isEncrypted:
                pdf.decrypt('')

            merged_file.append(pdf)

    with open(destination_path, 'wb') as output:
        merged_file.write(output)
    return True

def remove_slides(source_path, destination_path):
    number_of_pages = 0
    unique_pages = []

    unique_pdf = PdfFileWriter()

    with open(source_path, 'rb') as f:
        pdf = PdfFileReader(f)
        if pdf.isEncrypted:
            pdf.decrypt('')
        number_of_pages = pdf.getNumPages()

        for pages in range(number_of_pages):
            curr_page = ''.join(pdf.getPage(pages).extractText().split()[:-1])
            if pages == number_of_pages - 1:
                unique_pdf.addPage(pdf.getPage(pages))
                continue
            next_page = ''.join(pdf.getPage(pages + 1).extractText().split()[:-1])

            if curr_page in next_page:
                continue
            else:
                unique_pdf.addPage(pdf.getPage(pages))


        with open(destination_path, "wb") as output:
            unique_pdf.write(output)

if __name__ == '__main__':
    try:
        output_file_name = sys.argv[1]
        list_of_pdfs = list(filter(lambda x: x.startswith("slides"), os.listdir()))
        list_of_pdfs.sort()
        print(list_of_pdfs)
        if merge_files('merged.pdf', list_of_pdfs):
            remove_slides('merged.pdf', output_file_name)
            print("We are done!")
    except:
        print("Didn't enter file output name!")
        exit(1)
