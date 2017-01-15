#!/usr/bin/env python3
import argparse
import csv
from glob import glob
from io import StringIO, SEEK_SET
from itertools import chain
import sys

__version__ = '2017-01-15'

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='CSV to tab-separated text'
                                             ' converter.')
    ap.add_argument('csv_files', metavar='CSV_FILE', type=str, nargs='+',
                    help='CSV file(s) to convert.')
    ap.add_argument('-i', '--input-encoding', metavar='ENCODING', type=str,
                    default='utf-8', help='Character encoding of the CSV'
                                          ' file(s). (default:utf-8)')
    ap.add_argument('-o', '--output-encoding', metavar='ENCODING', type=str,
                    default='utf-8', help='Character encoding of the output.'
                                          ' (default:utf-8)')
    ap.add_argument('-d', '--dialect', type=str, default='excel',
                    help='CSV dialect. (default:excel)')
    ap.add_argument('-s', '--skip-rows', metavar='N', type=int, nargs='?',
                    default=0, help='Skip first N rows. (default:excel)')
    args = ap.parse_args()
    ienc = args.input_encoding
    oenc = args.output_encoding

    writer_buf = StringIO()
    writer = csv.writer(writer_buf, delimiter='\t', dialect=args.dialect)

    def convert(reader):
        for row in reader:
            writer.writerow(row)
            sys.stdout.buffer.write(writer_buf.getvalue().encode(oenc))
            writer_buf.seek(0, SEEK_SET)
            writer_buf.truncate()

    filenames = chain.from_iterable((glob(pat) for pat in args.csv_files))
    for filename in filenames:
        try:
            with open(filename, 'rt', newline='', encoding=ienc) as f:
                for i in range(args.skip_rows):
                    f.readline()
                reader = csv.reader(f, dialect=args.dialect)
                convert(reader)
        except Exception as ex:
            print('Error on processing "{}":'.format(filename),
                  file=sys.stderr)
            raise
