import json
import pyperclip
from html import escape

def create_html_table(data):
    html = '<table border="1">\n'

    for item in data:
        # First row with query and query type, and links to searches.
        html += '<tr>\n'
        html += f'<td><b>[{escape(item["query"])}]</b><br>'
        html += f'<small><i>Search on <a href="{item["currentSearch"]["link"]}">Pod</a> or </i>'
        html += f'<a href="{item["trieveSearch"]["link"]}">Trieve</a></small><br>'
        html += f'<small>{escape(item["queryType"])}</small>\n'
    
        # Second 'row' with two images.
        html += '<div style="display: flex; justify-content: space-between;">'
        html += f'<a href="{item["currentSearch"]["image"]}" target="_blank" style="width: 49%;">'
        html += f'<img src="{item["currentSearch"]["image"]}" '
        html += f'alt="{item["currentSearch"]["alt"]}" style="width: 100%; height: auto;">'
        html += '</a>\n'
        html += f'<a href="{item["trieveSearch"]["image"]}" target="_blank" style="width: 49%;">'
        html += f'<img src="{item["trieveSearch"]["image"]}" '
        html += f'alt="{item["trieveSearch"]["alt"]}" style="width: 100%; height: auto;">'
        html += '</a>\n'
        html += '</div>'
        html += '</td>\n'
        html += '</tr>\n'

        # Third row with comparison text if it exists.
        if "comparison" in item:
            html += '<tr>\n'
            comparison = item["comparison"].get("text", "")
            html += f'<td>{escape(comparison)}</td>\n'
            html += '</tr>\n'
        
        # Subsequent rows with query variants.
        if "queryVariants" in item:
            for variant in item["queryVariants"]:
                html += '<tr>\n'
                html += f'<td><small><b>[{escape(variant["query"])}]</b></small><br>\n'
                html += f'<small><i>Search on <a href="{variant["currentSearch"]["link"]}">Pod</a> or </i>'
                html += f'<a href="{variant["trieveSearch"]["link"]}">Trieve</a></small><br>\n'
                # Second 'row' with two images.
                html += '<div style="display: flex; justify-content: space-between;">'
                html += f'<a href="{variant["currentSearch"]["image"]}" target="_blank" style="width: 49%;">'
                html += f'<img src="{variant["currentSearch"]["image"]}" '
                html += f'alt="{variant["currentSearch"]["alt"]}" style="width: 100%; height: auto;">'
                html += '</a>\n'
                html += f'<a href="{variant["trieveSearch"]["image"]}" target="_blank" style="width: 49%;">'
                html += f'<img src="{variant["trieveSearch"]["image"]}" '
                html += f'alt="{variant["trieveSearch"]["alt"]}" style="width: 100%; height: auto;">'
                html += '</a>\n'
                html += '</div>'
                html += '</td>\n'
                html += '</tr>\n'

    html += '</table>'
    return html

# Load JSON data
with open('podfoods_comparisons.json', 'r') as f:
    data = json.load(f)

# Generate HTML table
html_table = create_html_table(data)

# Copy HTML table to clipboard


pyperclip.copy(html_table)
print("HTML table has been copied to clipboard")


# Write HTML table to file
with open('comparison_table.html', 'w') as f:
    f.write(html_table)

print("HTML table has been generated and saved as 'comparison_table.html'")
