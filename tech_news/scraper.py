import requests
import time
from parsel import Selector


URL_BASE = 'https://blog.betrybe.com/'


def fetch(URL_BASE):
    time.sleep(1)

    try:
        response = requests.get(
            URL_BASE,
            headers={"user-agent": "Fake user-agent"},
            timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.Timeout:
        return None


def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_urls = selector.css('.cs-overlay a::attr(href)').getall()
    if news_urls:
        return news_urls
    return []


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css('.next.page-numbers::attr(href)').get()
    if next_page:
        return next_page
    return None


def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css('.entry-title::text').get().strip()
    timestamp = selector.css('.meta-date::text').re_first(r'\d{2}/\d{2}/\d{4}')
    writer = selector.css('.author a::text').get()
    reading_time = int(selector.css('.meta-reading-time::text')
                       .get().split()[0])
    summary = (
        selector.css('div.entry-content > p')
        .xpath('string()')
        .get()
        .strip()
        )
    category = selector.css('.category-style .label::text').get()

    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'reading_time': reading_time,
        'summary': summary,
        'category': category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
