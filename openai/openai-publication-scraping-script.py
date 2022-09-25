from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd

def open_second_window(browser, link):
    link.click()
    sleep(3)
    browser.switch_to.window(browser.window_handles[1])

def close_second_window(browser):
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

def get_authors(browser, link):
    open_second_window(browser, link)
    author_links = browser.find_elements_by_css_selector('div.authors a')
    if not author_links:
        close_second_window(browser)
        return ''
    paper_authors = []
    for link in author_links:
        author = link.text
        paper_authors.append(author)
    author_string = ', '.join(paper_authors)
    print('authors:', author_string)
    close_second_window(browser)
    return author_string

def main():
    url = 'https://openai.com/publications'
    browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    browser.get(url)

    # get all the links from the page
    links = browser.find_elements_by_css_selector('h5.medium-xsmall-copy a')
    titles = []
    authors = []

    for link in links:
        # 1. get title
        title = link.text
        titles.append(title)
        print('title:', title)
        # 2. get authors from arxiv
        authors_of_paper = get_authors(browser, link)
        authors.append(authors_of_paper)

    df = pd.DataFrame({
        'titles': titles,
        'is_safety_paper': ['no' for _ in range(len(titles))],
        'authors': authors
    })
    df.to_csv('openai-papers-and-authors.csv')

if __name__ == '__main__':
    main()
