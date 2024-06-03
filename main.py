import os
import sys
import numpy as np
import pandas as pd

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(f"Hello, {name}! This is a test Python script.")
        generate_html_file(name)
        
        # Demonstrating the addition of two arrays using numpy
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        result_array = add_arrays(array1, array2)
        print(f"Result of adding {array1} and {array2} is: {result_array}")
        
        # Create a DataFrame using pandas
        df = pd.DataFrame({
            'Array1': array1,
            'Array2': array2,
            'Result': result_array
        })
        print(df)
    else:
        print("No name provided. This is a test Python script.")

def generate_html_file(name):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Application Output</title>
</head>
<body>
    <h1>Python Application Output</h1>
    <div id="output">
        <p>Hello, {name}! This is a test file.</p>
    </div>
</body>
</html>"""
    
    docs_dir = "docs"
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)
    
    with open(os.path.join(docs_dir, "index.html"), "w") as file:
        file.write(html_content)

def add_arrays(array1, array2):
    """Adds two arrays element-wise using numpy."""
    return np.add(array1, array2)

if __name__ == "__main__":
    main()
