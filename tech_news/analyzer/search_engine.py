from tech_news.database import db


def search_by_title(title):
    news = db.news.find({"title": {"$regex": title, "$options": "i"}})
    result = [(item["title"], item["url"]) for item in news]
    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
