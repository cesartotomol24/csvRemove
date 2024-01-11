import os
import pandas as pd

# Specify the input directory containing CSV files
input_directory = './Prueba1'

# Specify the output directory for saving modified CSV files
output_directory = './Output1'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List all CSV files in the input directory
csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

# Iterate through each CSV file
for file in csv_files:
    # Construct the full path for input and output files
    input_file_path = os.path.join(input_directory, file)
    output_file_path = os.path.join(output_directory, f'output_without_cve_{file}')

    # Read CSV file into a DataFrame
    data = pd.read_csv(input_file_path)

    # Display
    print(f"Original '{file}' CSV Data: \n")
    print(data)

    # Remove 'data' column
    data.pop('columna_a_eliminar')

    # Display
    print(f"\nCSV Data after deleting the column 'data':\n")
    print(data)

    # Save the modified DataFrame to a new CSV file
    data.to_csv(output_file_path, index=False)

    print(f"The 'cve' column has been removed. Output saved to {output_file_path}\n")
