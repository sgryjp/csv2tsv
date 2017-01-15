# csv2tsv
Command to convert CSV files to tab-separated text files.

## Prerequesties

- Python 3.2 or later

## Usage
```
usage: csv2tsv.py [-h] [-i ENCODING] [-o ENCODING] [-d DIALECT] [-s [N]]
                  CSV_FILE [CSV_FILE ...]

CSV to tab-separated text converter.

positional arguments:
  CSV_FILE              CSV file(s) to convert.

optional arguments:
  -h, --help            show this help message and exit
  -i ENCODING, --input-encoding ENCODING
                        Character encoding of the CSV file(s). (default:utf-8)
  -o ENCODING, --output-encoding ENCODING
                        Character encoding of the output. (default:utf-8)
  -d DIALECT, --dialect DIALECT
                        CSV dialect. (default:excel)
  -s [N], --skip-rows [N]
                        Skip first N rows. (default:excel)
```

## Notes

- By default, `csv2tsv` uses dialect of CSV format which is used by Microsoft Excel.
- Tested only on macOS 10.12 (Sierra)

## Example

To convert CSV file(s) into text file:
```
$ csv2tsv.py a.csv > a.txt
$ csv2tsv.py a.csv b.csv > a_and_b.txt
```

This example converts content (excluding the column-header line) of multiple CSV files and writes it into a single text file.
```
$ head -n 1 stat-2016-01.csv > stat-2016.txt
$ csv2tsv.py -s 1 stat-2016-??.csv >> stat-2016.txt
```

To convert CSV file(s) and copy it into the system's clipboard:
- For Mac:
  ```
  $ csv2tsv.py a.csv | pbcopy
  ```
- For Windows (not tested yet):
  ```
  C:\> csv2tsv.py a.csv | clip
  ```
