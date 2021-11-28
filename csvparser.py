import csv

def readcsvFile(filename):
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar=',')
        for row in spamreader:
            print(', '.join(row))

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                print("file di test semplice " + row['organization'], row['alone'])
                print("file di test complesso " + row['CLIENTE,'], row['LOTTO,'])
            except:
                print("keys not found")