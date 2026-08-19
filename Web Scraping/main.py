from bs4 import BeautifulSoup
import requests

for pagina in range(1,51):
    url=f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    print(url)