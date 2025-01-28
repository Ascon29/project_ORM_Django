from django.urls import path
from library.apps import LibraryConfig
from .views import BooksListView, BookCreateView, BookDeleteView, BookDetailView, BookUpdateView, AutorCreateView, \
    AutorUpdateView, AutorListView, RecommendBookView, ReviewBookView

app_name = LibraryConfig.name


urlpatterns = [
    path('autor/new/', AutorCreateView.as_view(), name='autor_create'),
    path('autor/update/<int:pk>/', AutorUpdateView.as_view(), name='autor_update'),
    path('autors/', AutorListView.as_view(), name='autors_list'),

    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/new', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('books/recommend/<int:pk>/', RecommendBookView.as_view(), name='book_recommend'),
    path('books/review/<int:pk>/', ReviewBookView.as_view(), name='book_review'),
]
