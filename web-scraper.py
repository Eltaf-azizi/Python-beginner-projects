import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract useful information from the website
        # For example, let's extract headlines from a news website
        headlines = []
        for headline in soup.find_all('h2'):
            headlines.append(headline.text.strip())
        
        return headlines
    else:
        print("Failed to scrape website:", response.status_code)
        return None

def main():
    url = "https://example.com"  # Replace with the URL of the website you want to scrape
    headlines = scrape_website(url)
    
    if headlines:
        print("Headlines:")
        for headline in headlines:
            print("-", headline)
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
