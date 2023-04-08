import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://www.free-ebooks.net'

book_links = []
for x in range(1,5):
    res = requests.get(f'https://www.free-ebooks.net/sci-fi-fantasy/{x}')
    soup = BeautifulSoup(res.text, 'html.parser')
    booklist = soup.find_all('h3', class_='tlc')
    for item in booklist:
        for links in item.find_all('a', href=True):
            book_links.append(base_url+links['href'])

book_details =[]

for link in book_links:
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.find('h1').text
    author = soup.find('p').find('a').text
    book = {
        'name':name,
        'author':author
    }
    book_details.append(book)
# Creating a pandas dataframe
df = pd.DataFrame(book_details)

# Converting it to csv file
df.to_csv(r"C:\Users\DUMKA\Desktop\book.csv")


