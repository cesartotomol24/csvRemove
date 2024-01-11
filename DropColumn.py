#Elimina columnas de un CSV

# import pandas with shortcut 'pd'
import pandas as pd

# read_csv function which is used to read the required CSV file
data = pd.read_csv('Archivo.csv')

# display
print("Original 'input.csv' CSV Data: \n")
print(data)

# pop function which is used in removing or deleting columns from the CSV files
data.pop('Columna_a_Borrar')

# display
print("\nCSV Data after deleting the column 'cve':\n")
print(data)

# save the modified DataFrame to a new CSV file
output_file = 'output_cve.csv'
data.to_csv(output_file, index=False)

print(f"The column has been removed. Output saved to {output_file}")

