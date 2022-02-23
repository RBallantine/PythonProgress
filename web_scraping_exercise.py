'''
    Ronan Ballantine
    23/02/2022
    Web scraping exercise
    
    Scrapes the first 4 pages of book listings on toscrape.com 
    and displays a list of books that are rated five stars.
'''

import requests
import bs4

books_url = 'https://books.toscrape.com/catalogue/category/books_1/page-{}.html'

five_star_titles = []

for n in range(1,5):

    result = requests.get(books_url.format(n))
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Five')) != 0:
            book_title = book.select('a')[1]['title']
            five_star_titles.append(book_title)

print(*five_star_titles, sep='\n')
