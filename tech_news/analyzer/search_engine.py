from tech_news.database import db
from datetime import datetime


def search_by_title(title):
    news = db.news.find({"title": {"$regex": title, "$options": "i"}})
    result = [(item["title"], item["url"]) for item in news]
    return result


def search_by_date(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date_db_format = date_obj.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    news = db.news.find({"timestamp": date_db_format})
    result = [(item["title"], item["url"]) for item in news]
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
