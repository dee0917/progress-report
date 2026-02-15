
import json
import os

json_path = r'c:\Users\Dee\MyApp\work\projects\progress-report\extracted_products.json'
output_path = r'c:\Users\Dee\.gemini\antigravity\brain\d2a99550-e067-4e00-bef6-d9497aa35dc8\extracted_product_data.md'

with open(json_path, 'r', encoding='utf-8') as f:
    categories = json.load(f)

total_categories = len(categories)
total_products = sum(len(cat['items']) for cat in categories)

markdown_content = f"# Extracted Product Data Analysis\n\n"
markdown_content += f"**Total Categories:** {total_categories}\n"
markdown_content += f"**Total Products:** {total_products}\n\n"
markdown_content += "---\n\n"

for cat in categories:
    cat_title = cat.get('title', cat.get('id', 'Unknown Category'))
    # Clean up title if it contains ##
    cat_title = cat_title.replace('## ', '').strip()
    
    markdown_content += f"## {cat_title}\n\n"
    markdown_content += f"**Product Count:** {len(cat['items'])}\n\n"
    
    markdown_content += "| ID | Name | Weight | Price | URL |\n"
    markdown_content += "|---|---|---|---|---|\n"
    
    for item in cat['items']:
        name = item.get('name', 'N/A')
        item_id = item.get('id', 'N/A')
        weight = item.get('weight', 'N/A')
        price = item.get('price', 'N/A')
        url = item.get('url', '#')
        
        markdown_content += f"| {item_id} | {name} | {weight} | {price} | [Link]({url}) |\n"
    
    markdown_content += "\n"

with open(output_path, 'w', encoding='utf-8') as out:
    out.write(markdown_content)

print(f"Report generated at {output_path}")
