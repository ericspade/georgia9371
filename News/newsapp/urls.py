from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, ArticlesList, NewsDetail, ArticlesDetail, NewsCreate, ArticleCreate, NewsUpdate, \
    ArticleUpdate, NewsDelete, ArticleDelete, subscribe

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('news/', NewsList.as_view(), name='news'),
    path('articles/', ArticlesList.as_view(), name='news'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('news/<int:pk>', NewsDetail.as_view(), name='news'),
    path('articles/<int:pk>', ArticlesDetail.as_view(), name='news'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('news/subscribe/', subscribe, name='subscribe'),
    path('articles/subscribe/', subscribe, name='subscribe'),
]
