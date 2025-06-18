import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']


url = 'https://habr.com/ru/articles/' # url для парсинга


response = requests.get(url)
response.raise_for_status()  # Проверяем, успешен ли запрос

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('li', class_ = 'content-list__item content-list__item_post shortcuts_item')

for article in articles:
    title = article.find("h2", class_ = "post_title")
    if not title:
        continue
    title = title.text.strip()