from tech_news.database import db


def top_5_categories():
    top_5 = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]

    categories = list(db.news.aggregate(top_5))
    result = [category["_id"] for category in categories]
    return result
