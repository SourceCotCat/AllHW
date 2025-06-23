import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init()

KEYWORDS = ['криптовалюты', 'жизнь', 'OpenAI', 'ресурс', 'лабубу'] # Определяем список ключевых слов:

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

    date_tg = article.find('time')
    date = date_tg['datetime'][:10] if date_tg else 'Дата не найдена' # дата нашей статьи (вез времени) формат year-month-day

    try:
        article_response = requests.get(link)
        article_response.raise_for_status()
        article_soup = BeautifulSoup(article_response.text, 'html.parser')

        body = article_soup.find('div', {'class': lambda c: c and 'article-formatted-body' in c}) # Ищем основной текст статьи
        full_text = body.get_text(strip=True).lower() if body else ''

        cot = article_soup.find('div', class_='tm-publication-hubs')
        tags = []
        if cot:
            tag_links = cot.find_all('a', class_='tm-publication-hub__link')
            tags = [tag.get_text(strip=True).lower() for tag in tag_links]

        match_in_title = any(keyword in title.lower() for keyword in KEYWORDS)
        match_in_text = any(keyword in full_text for keyword in KEYWORDS)
        match_in_tags = any(keyword in ' '.join(tags) for keyword in KEYWORDS)

        # Проверяем наличие любого из ключевых слов в заголовке, тексте или тегах
        if match_in_title or match_in_text or match_in_tags:
            reasons = []
            if match_in_title:
                reasons.append(f"{Fore.YELLOW}в заголовке{Style.RESET_ALL}")
            if match_in_text:
                reasons.append(f"{Fore.CYAN}в тексте{Style.RESET_ALL}")
            if match_in_tags:
                reasons.append(f"{Fore.MAGENTA}в тегах{Style.RESET_ALL}")
        
        print(f"{Fore.GREEN}ё{date} – {title} – {link}{Style.RESET_ALL} ({', '.join(reasons)})")

    except Exception as e:
        print(f"{Fore.RED}Ошибка при обработке статьи: {link}{Style.RESET_ALL}")
    
    # print(f"Title: {title}")
    # print(f"link: {link}")
    # print(f"date: {date}")
    # print('---------')