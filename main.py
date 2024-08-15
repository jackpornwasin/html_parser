import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_html(url):
    # Fetch the page content
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def filter_urls(a_tags, pattern, prepend = None):
    urls = []
    for a_tag in a_tags:
        href = a_tag['href']
        # Filter URLs based on the prefix
        if href.startswith(pattern):
            href = prepend + href if prepend else href
            urls.append(href)
    return urls

def extract_month_year(paragraph):
    # Regular expression to find the month and year
    match = re.search(r'completed in (\w+) (\d{4})', paragraph)
    if match:
        month = match.group(1)
        year = match.group(2)
        return month, year
    return None, None

if __name__ == "__main__":
    # Neighborhood page
    url = "https://www.hipflat.co.th/en/mass-transit/bts-phrom-phong-jfahsqsx"
    html_content = extract_html(url)

    url_list = html_content.find_all('a', attrs={"data-test":  "project-link"}, href=True)
    urls = filter_urls(url_list, "/en/projects/", "https://www.hipflat.co.th")

    result_set = []
    for url in urls:
        # Build page
        html_content = extract_html(url)

        # first element of span tag css class description__about
        try:
            build_name = html_content.find_all("span", "description__about")[0].text
            build_name = build_name[len("Overview of "):]
        except:
            build_name = None
        
        # First element of p tag css class name description__generated
        try:
            paragraph = html_content.find_all("p", "description__generated")[0]
            month, year = extract_month_year(paragraph.text)
        except:
            year = None

        result_set.append({"Build": build_name, "Year": year, "URL": url})

    # write to excel    
    df = pd.DataFrame(result_set)
    df.to_csv("output.csv")