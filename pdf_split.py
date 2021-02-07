#!/usr/bin/env python3

#-m pip3 install pypdf2
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in', type=str, nargs='+', dest='pdfs_to_merge', required=True, help='List of pdf fragments to merge')
    parser.add_argument('--out', type=str, dest='output_name', required=True, help='Output pdf name')
    return parser.parse_args()


def merge_pdfs(pdfs_to_merge, output_name):
    print('FROM:', pdfs_to_merge)
    print('TO  :', output_name)

    output = PdfFileWriter()
    inputs = []
    total_pages = 0
    for input_pdf_path in pdfs_to_merge:
        input_file = open(input_pdf_path, "rb")
        input_pdf = PdfFileReader(input_file)

        print('Reading', input_pdf_path, 'with', input_pdf.numPages, 'pages...')

        for i in range(0, input_pdf.numPages):
            output.addPage(input_pdf.getPage(i))
            total_pages += 1
        inputs.append(input_file)

    with open(output_name, "wb") as outputStream:
        output.write(outputStream)

    for input_file in inputs:
        input_file.close()

    print('Merge completed:', output_name, 'with', total_pages, 'pages.')


def main():
    args = parse_args()
    merge_pdfs(args.pdfs_to_merge, args.output_name)


if __name__ == '__main__':
    main()
