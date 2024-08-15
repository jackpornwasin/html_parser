
# HTML Parser

HTML Parser is a Python utility designed to extract and process specific elements from HTML files. This tool is particularly useful for developers who need to parse HTML documents and extract data based on custom rules.

## Features

- **Tag Extraction**: Extract all HTML elements by their tag name.
- **Class-based Filtering**: Filter elements by their `class` attribute.
- **ID-based Filtering**: Retrieve elements based on their `id` attribute.
- **Text Content Extraction**: Extract and print the text content of HTML elements.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/jackpornwasin/html_parser.git
cd html_parser
pip install -r requirements.txt
```

## Usage

Here’s how you can use the HTML Parser:

### Extracting by Tag

To extract all elements of a specific tag (e.g., `div`):

```python
from main import HTMLParser

# Initialize the parser with your HTML file
parser = HTMLParser('path/to/your/file.html')

# Extract elements by tag
elements = parser.extract_by_tag('div')
for element in elements:
    print(element)
```

### Filtering by Class

To filter elements by their `class` attribute:

```python
# Extract elements by tag and filter by class
elements = parser.extract_by_class('div', 'your-class-name')
for element in elements:
    print(element)
```

### Filtering by ID

To retrieve a specific element by its `id` attribute:

```python
# Extract an element by its ID
element = parser.extract_by_id('your-element-id')
print(element)
```

### Extracting Text Content

To extract and print the text content of an element:

```python
# Extract text content from a tag
text_content = parser.extract_text_content('p')
print(text_content)
```

### Combining Filters

You can combine filters for more precise extraction:

```python
# Extract elements by tag and filter by both class and ID
elements = parser.extract_by_class('div', 'your-class-name')
for element in elements:
    if parser.has_id(element, 'your-element-id'):
        print(parser.extract_text_content(element))
```
