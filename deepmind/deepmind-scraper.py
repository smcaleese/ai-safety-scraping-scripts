from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_papers_and_authors(soup, papers_and_authors):
    papers = soup.find_all('div', class_='c_card_list__item__container')
    for paper in papers:
        title = paper.find(attrs={'fs-cmsfilter-field': 'title'}).get_text()
        print('title:', title)
        author_elements = paper.find_all(attrs={'fs-cmsfilter-field': 'authors'})
        for e in author_elements:
            authors_string = e.get_text()
            for char in ['\n', ' *']:
                authors_string = authors_string.replace(char, '')
            author_names = authors_string.split(',')
        papers_and_authors[title] = author_names

def main():
    url = 'https://www.deepmind.com/research?tag=Safety&d907cb24_page=1'    # get all publications related to AI safety
    papers_and_authors = {}
    browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    browser.get(url)
    next_buttons = browser.find_elements(By.CLASS_NAME, 'c_card_list__pagination__children__link')

    for i, button in enumerate(next_buttons):
        print(f'clicked to page {i + 1}')
        button.click()
        time.sleep(1)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        get_papers_and_authors(soup, papers_and_authors)

    print('papers and authors:', papers_and_authors, len(papers_and_authors.keys()))

    df = pd.DataFrame({
        'titles': papers_and_authors.keys(),
        'authors': [', '.join(arr) for arr in papers_and_authors.values()]
    })
    df.to_csv('deepmind-papers-and-authors.csv')

if __name__ == '__main__':
    main()
