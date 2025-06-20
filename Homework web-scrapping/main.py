import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']


url = 'https://habr.com/ru/articles/' # url для парсинга


response = requests.get(url)
response.raise_for_status()  # Проверяем, успешен ли запрос

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article', class_ = 'tm-articles-list__item') # ищем статьи на странице

print('Найдены статьи по ключевым словам:')

for article in articles:
    title_tg = article.find('a', class_ = 'tm-title__link') 
    if not title_tg:
        continue
    title = title_tg.get_text(strip=True) # наш заголовочек статьи
    link = 'https://habr.com' + title_tg['href']

    print(f"Title: {title}")
    print(f"link: {link}")
    print('---------')

print('мда треш')