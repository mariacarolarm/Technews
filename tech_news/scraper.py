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


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
