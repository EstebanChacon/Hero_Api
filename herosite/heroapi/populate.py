import csv
CSV_FILE = '../../superhero_dataset_full/superheroes_nlp_dataset.csv'
with open(CSV_FILE, newline='', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"' )
    for line in csv_reader:
        print(line[0])
