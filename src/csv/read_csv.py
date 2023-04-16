import csv

csv_file_path=r'Z:\___advanced python\movies.csv'
with open(csv_file_path, 'r+', encoding='utf-8') as cf:
    csv_opened = csv.reader(cf)
    print(type(csv_opened))