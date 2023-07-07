from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .pagination import CustomPageNumberPagination

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class=CustomPageNumberPagination
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
