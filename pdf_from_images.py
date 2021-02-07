#!/usr/bin/env python3

#-m pip3 install fpdf, pillow
import os
from fpdf import FPDF
import argparse
from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in', type=str, nargs='+', dest='image_files', required=True, help='Image files to insert into PDF')
    parser.add_argument('--out', type=str, dest='output_name', required=True, help='Output PDF name')
    return parser.parse_args()


def create_pdf(image_files, output_name):
    pdf = FPDF("P", "mm", "Letter")
    
    for image_file in image_files:
        print('Inserting', image_file, '...')

        im = Image.open(image_file)
        (image_w, _) = im.size

        pdf.add_page()
        if image_w > 150:
            image_w = 150

        cx = 216 / 2
        x = cx - image_w/2
        pdf.image(image_file, x, 20, w=image_w)

    pdf.output(output_name, 'F')

    print('Done. See', output_name)


def main():
    args = parse_args()
    create_pdf(args.image_files, args.output_name)


if __name__ == '__main__':
    main()
