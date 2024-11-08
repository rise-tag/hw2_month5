from django.urls import path
from .views import NewsListAPI, NewsCreateAPI, NewsRetrieveAPI, NewsUpdateAPI, NewsDestroyAPI

urlpatterns = [
    path('news/', NewsListAPI.as_view(), name='news-list'),  
    path('news/create/', NewsCreateAPI.as_view(), name='news-create'),
    path('news/<int:pk>/', NewsRetrieveAPI.as_view(), name='news-retrieve'),
    path('news/<int:pk>/update/', NewsUpdateAPI.as_view(), name='news-update'),  
    path('news/<int:pk>/delete/', NewsDestroyAPI.as_view(), name='news-delete'),  
]
