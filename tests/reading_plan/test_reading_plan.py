from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest


def test_reading_plan_group_news(mocker):
    mock_news_data = [
        {"title": "Notícia 1", "reading_time": 2},
        {"title": "Notícia 2", "reading_time": 3},
        {"title": "Notícia 3", "reading_time": 6},
        {"title": "Notícia 4", "reading_time": 17},
        {"title": "Notícia 5", "reading_time": 12},
        {"title": "Notícia 6", "reading_time": 13},
    ]
    mocker.patch("tech_news.analyzer.reading_plan.find_news",
                 return_value=mock_news_data)

    with pytest.raises(ValueError,
                       match="Valor 'available_time' deve ser maior que zero"):
        ReadingPlanService.group_news_for_available_time(0)

    available_time = 10
    result = ReadingPlanService.group_news_for_available_time(available_time)

    expected_result = {
        "readable": [
            {
                "unfilled_time": 5,
                "chosen_news": [
                    ("Notícia 1", 2),
                    ("Notícia 2", 3),
                ],
            },
            {
                "unfilled_time": 4,
                "chosen_news": [
                    ("Notícia 3", 6),
                ],
            },
        ],
        "unreadable": [
            ("Notícia 4", 17),
            ("Notícia 5", 12),
            ("Notícia 6", 13),
        ],
    }

    assert result == expected_result


def test_wrong_unfilled_time(mocker):
    mock_news_data = [
        {"title": "Notícia 1", "reading_time": 2},
        {"title": "Notícia 2", "reading_time": 3},
    ]
    mocker.patch("tech_news.analyzer.reading_plan.find_news",
                 return_value=mock_news_data)
    result = ReadingPlanService.group_news_for_available_time(5)

    for group in result['readable']:
        total_reading_time = sum([news[1] for news in group['chosen_news']])
        assert group['unfilled_time'] == 5 - total_reading_time


def test_empty_unreadable_news(mocker):
    mock_news_data = [
        {"title": "Notícia 1", "reading_time": 2},
        {"title": "Notícia 2", "reading_time": 3},
    ]
    mocker.patch("tech_news.analyzer.reading_plan.find_news",
                 return_value=mock_news_data)
    result = ReadingPlanService.group_news_for_available_time(5)

    assert not result['unreadable']
    total_readable_news = sum(len(group['chosen_news'])
                              for group in result['readable'])
    assert total_readable_news == len(mock_news_data)


def test_duplicate_unreadable_news(mocker):
    mock_news_data = [
        {"title": "Notícia 1", "reading_time": 10},
        {"title": "Notícia 2", "reading_time": 20},
        {"title": "Notícia 1", "reading_time": 10},
    ]
    mocker.patch("tech_news.analyzer.reading_plan.find_news",
                 return_value=mock_news_data)
    result = ReadingPlanService.group_news_for_available_time(5)

    unreadable_titles = [news[0] for news in result['unreadable']]
    assert len(unreadable_titles) != len(set(unreadable_titles))
    assert unreadable_titles.count("Notícia 1") == 2
