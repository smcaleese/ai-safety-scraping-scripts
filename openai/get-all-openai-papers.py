from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

def main():
    url = 'https://openai.com/publications'
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    paper_elements = soup.find_all('h5', class_='medium-xsmall-copy')

    links = []
    for e in paper_elements:
        link = e.find('a')
        links.append(link.get_text())

    df = pd.DataFrame({'paper': links})
    df.to_csv('openai-papers-and-authors.csv')

if __name__ == '__main__':
    main()
