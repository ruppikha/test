import os
import sys

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(f"Hello, {name}! This is a test Python script.")
        generate_html_file(name)
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

if __name__ == "__main__":
    main()
