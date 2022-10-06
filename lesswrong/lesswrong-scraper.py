from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def main():
    url = 'https://www.lesswrong.com/allPosts?sortedBy=new'
    browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    browser.maximize_window()
    browser.get(url)

    time.sleep(10)

    # Load more posts by clicking the 'load more' button
    for i in range(20):
        try:
            more_button = browser.find_element(By.LINK_TEXT, 'Load More Days')
            more_button.click()
            print(f'loading more posts ({i + 1})')
            time.sleep(5)
        except NoSuchElementException:
            continue

    # Get the authors using BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    posts = soup.find_all('div', class_='PostsItem2-root')

    authors = []
    titles = []
    dates = []

    for post in posts:
        try:
            title = post.find('span', class_='PostsItem2-title').get_text()
            authors_list = post.find('span', class_='PostsItem2-author').get_text()
            date = post.find('span', class_='PostsItemDate-postedAt').get_text()
            print('title:', title, 'authors:', authors, 'date:', date)
            titles.append(title)
            authors.append(authors_list)
            dates.append(date)
        except Exception:
            continue

    df = pd.DataFrame({
        'titles': titles,
        'authors': authors,
        'dates': dates
    })
    df.to_csv('lw-posts-and-authors.csv')

if __name__ == '__main__':
    main()
