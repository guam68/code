import pandas
import openpyxl
import sys

try:
    file_name = sys.argv[1]
except:
    print('\nJson file name (no extension) required as argument. Optional 2nd arg for output file.\n')
    raise SystemExit
try:
    output_file = sys.argv[2]
except:
    output_file = 'output'

with open(file_name + '.json') as f:
    pandas.read_json(f).to_excel(output_file + '.xlsx')