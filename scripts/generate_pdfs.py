import os
import subprocess

current_working_directory = os.getcwd()
print("Current Working Directory:", current_working_directory)

def convert_notebook_to_pdf(notebook_path, output_path):
    print(f"Trying to convert {notebook_path} to {output_path}.pdf")
    try:
        subprocess.run(["jupyter", "nbconvert", notebook_path, "--to", "pdf", "--output", output_path])
        print(f"Successfully converted {notebook_path} to {output_path}.pdf")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
notebook_path = os.path.join(current_working_directory, 'lessons/Wk0/L01.ipynb')
output_path = os.path.join(current_working_directory, 'lessons/Wk0/L01')

# Check if the file exists at the given path
if os.path.exists(notebook_path):
    print(f"File exists: {notebook_path}")
else:
    print(f"File does not exist: {notebook_path}")

convert_notebook_to_pdf(notebook_path, output_path)
