import csv

with open('csv_aula.csv', 'r') as arquio_csv:
    leitor_csv = csv.reader(arquio_csv, delimiter=';')
    for linha in leitor_csv:
        print(linha)