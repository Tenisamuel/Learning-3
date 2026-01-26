import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No title found"
    print(f"\nPage Title: {title}\n")

    print("Links found on the page:")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            print(href)


if __name__ == "__main__":
    website = "https://example.com"
    scrape_website(website)