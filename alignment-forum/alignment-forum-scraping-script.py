from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def main():
    url = 'https://www.alignmentforum.org'
    browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    browser.maximize_window()
    browser.get(url)

    # Load more posts using selenium 
    for i in range(10):
        try:
            more_button = browser.find_element(By.CSS_SELECTOR, 'a.LoadMore-sectionFooterStyles')
            more_button.click()
            print(f'loading more posts ({i + 1})')
            time.sleep(5)
        except NoSuchElementException:
            continue

    # Get the authors using BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    posts = soup.find_all('div', class_='PostsItem2-postsItem')

    authors = []
    titles = []

    for post in posts:
        try:
            title = post.find('span', class_='PostsItem2-title').get_text()
            authors_list = post.find('span', class_='PostsItem2-author').get_text()
            print('title:', title, 'authors:', authors)
            titles.append(title)
            authors.append(authors_list)
        except Exception:
            continue

    df = pd.DataFrame({
        'titles': titles,
        'authors': authors
    })
    df.to_csv('alignment-forum-posts-and-authors.csv')

if __name__ == '__main__':
    main()
