import csv
path='https://github.com/dheekshithbg/csvextract/blob/main/demonew.xlsx'
with open(path,newline=") as f:
          reader=csv.reader(f)
          for row in reader:
                     print(row)
