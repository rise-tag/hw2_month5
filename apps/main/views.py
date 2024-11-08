from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .models import News
from .serializers import NewsSerializer, NewsUpdateSerializer

# Просмотр всех новостей
class NewsListAPI(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Создание новости
class NewsCreateAPI(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Просмотр одной новости по ID
class NewsRetrieveAPI(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Обновление новости (только описание)
class NewsUpdateAPI(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer

# Удаление новости
class NewsDestroyAPI(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
