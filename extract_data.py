
import re
import json
import os

file_path = r'c:\Users\Dee\MyApp\work\projects\progress-report\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Look for const SOURCING_RAW = [ ... ];
# We use a pattern that captures everything inside the brackets
pattern = r'const SOURCING_RAW\s*=\s*(\[[\s\S]*?\]);'
match = re.search(pattern, content)

if match:
    json_str = match.group(1)
    try:
        data = json.loads(json_str)
        print(f"Successfully extracted {len(data)} categories.")
        
        # Save to file
        output_path = r'c:\Users\Dee\MyApp\work\projects\progress-report\extracted_products.json'
        with open(output_path, 'w', encoding='utf-8') as out:
            json.dump(data, out, indent=2, ensure_ascii=False)
        print(f"Data saved to {output_path}")
        
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        # Identify where the error is
        lines = json_str.split('\n')
        if e.lineno <= len(lines):
             print(f"Error at line {e.lineno}: {lines[e.lineno-1]}")
else:
    print("Could not find SOURCING_RAW data in file.")
