import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        ##obtener el nombre de las columnas
        header = next(reader)
        data = []
        for row in reader: 
            ##crear tuplas de los valores con el nombre de su columna
            iterable = zip(header, row)
            ##ya leimos el archivo, debemos transformarlo a un diccionario para poder leer la información más facilmente
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data
    
if __name__ == "__main__":
    data = read_csv(r"C:\Users\Usuario\Desktop\Python\app\data.csv")
