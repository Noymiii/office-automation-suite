import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_prices(url, output_file="competitor_prices.csv"):
    """
    Scrapes book titles and prices from a demo retail site.
    """
    # Headers make the request look like a real browser (Anti-blocking technique)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"🌐 Connecting to: {url}...")

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Check for 404 or 500 errors
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection Failed: {e}")
        return

    # 1. Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('article', class_='product_pod')

    extracted_data = []

    print(f"👀 Found {len(products)} items. Extracting data...")

    # 2. Extract Data
    for item in products:
        try:
            title = item.h3.a['title']
            # Price usually comes with a currency symbol, e.g., £51.77
            price_text = item.find('p', class_='price_color').text
            
            # Clean price data (remove currency symbol)
            price = price_text.replace('£', '')
            
            extracted_data.append([title, price])
        except AttributeError:
            continue

    # 3. Save to CSV
    if extracted_data:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Product Name', 'Price (GBP)']) # Header
            writer.writerows(extracted_data)
        print(f"✅ Data saved to {output_file}")
    else:
        print("⚠️ No product data found.")

if __name__ == "__main__":
    # A safe sandbox site for scraping practice
    target_url = "http://books.toscrape.com/" 
    scrape_prices(target_url)