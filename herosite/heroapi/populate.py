import csv
with open('/home/tpuser/Documents/projets/Hero_Api/superhero_dataset_full/superheroes_nlp_dataset.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"' )
    for row in csv_reader:
        print(', '.join(row))
