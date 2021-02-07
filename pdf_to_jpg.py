#!/usr/bin/env python3

#-m pip3 install wand
from wand.image import Image
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in', type=str, dest='input_pdf', required=True, help='PDF file to read pages')
    parser.add_argument('--out', type=str, dest='output_name', required=True, help='Output file pattern')
    return parser.parse_args()


def convert_to_images(input_pdf, output_name):
    print('Reading', input_pdf, '...')
    with Image(filename=input_pdf, resolution=300) as img:
        print('  item count = ', len(img.sequence))
        print('  saving items...')
        img.save(filename=output_name)
        print('Done')


def main():
    args = parse_args()
    convert_to_images(args.input_pdf, args.output_name)


if __name__ == '__main__':
    main()
