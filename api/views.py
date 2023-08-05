from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from articles.models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class ArticleListAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
