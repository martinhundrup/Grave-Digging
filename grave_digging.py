import json
import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# Define the base URL and total number of pages to loop through
base_url = "https://www.findagrave.com/cemetery/214432/memorial-search?cemeteryName=Pullman+City+Cemetery&page="
total_pages = 224

# Define the output list for storing scraped data
scraped_data = []

def get_page_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless mode if preferred
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        )
        
        # Open a new page in the context
        page = context.new_page()

        # Navigate to the URL
        page.goto(url, timeout=60000)
        
        # Wait for the specific content to load
        page.wait_for_selector("b.birthDeathDates.fw-light.fs-5.text-body", timeout=60000)
        time.sleep(5)  # Additional wait to ensure all JS data loads

        # Get the HTML content after loading
        content = page.content()
        
        # Close the browser
        browser.close()
        return content

# Loop through each page and extract data
for page_num in range(1, total_pages + 1):
    url = f"{base_url}{page_num}"
    print(f"Processing page {page_num}...")

    # Get the page content
    html_content = get_page_content(url)

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract relevant data for each page
    dates = soup.find_all('b', class_="birthDeathDates fw-light fs-5 text-body")
    for date in dates:
        # Create a dictionary for each item and add it to the list
        scraped_data.append({
            "birthDeathDate": date.get_text(strip=True)
        })
    
    # Optional: Pause between requests to avoid triggering bot protection
    time.sleep(2)  # Adjust sleep time if needed

# Write the scraped data to a JSON file
with open("scraped_data.json", "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, ensure_ascii=False, indent=4)

print("Data scraping complete. Saved to scraped_data.json.")
