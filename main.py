# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import re
import os
import os
import re

def convert_html_to_django(html_content):
    # Add {% load static %} at the top if not present
    if '{% load static %}' not in html_content:
        html_content = '{% load static %}\n' + html_content

    # Replace src="..." for local assets
    def replace_src(match):
        src_link = match.group(1)
        if src_link.startswith('http') or src_link.startswith('//'):
            return f'src="{src_link}"'  # Keep external links unchanged
        return f'src="{{% static \'{src_link}\' %}}"'

    html_content = re.sub(r'src="([^"]+)"', replace_src, html_content)

    # Replace href="..." for CSS and JS files only
    def replace_href(match):
        link = match.group(1)
        if link.startswith('http') or link.startswith('//'):
            return f'href="{link}"'  # Keep external links unchanged
        if link.endswith('.css') or link.endswith('.js'):
            return f'href="{{% static \'{link}\' %}}"'
        else:
            return f'href="{link}"'

    html_content = re.sub(r'href="([^"]+)"', replace_href, html_content)

    return html_content

def convert_file(input_path, output_path):
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    django_html = convert_html_to_django(html_content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(django_html)

    print(f"Converted file saved to {output_path}")

# Usage
input_path = 'index.html'
output_path = 'template/index.html'
convert_file(input_path, output_path)


