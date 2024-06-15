from django.urls import path

from books import views

urlpatterns = [
    path('', views.base, name='base'),
    path('book_info/<int:book_id>', views.book_info, name='book_info'),
    path('add_book', views.add_book, name='add_book'),
    path('add_cat', views.add_cat, name='add_cat'),
    path('delete_book/<int:book_id>', views.delete_book, name='delete_book'),
    path('delete_cat/<int:cat_id>', views.delete_cat, name='delete_cat'),
    path('delete_author/<int:author_id>', views.delete_author, name='delete_author'),
    path('add_author', views.add_author, name='add_author'),
    path('edit_book/<int:book_id>', views.edit_book, name='edit_book'),
    path('edit_cat/<int:cat_id>', views.edit_cat, name='edit_cat'),
    path('edit_author/<int:author_id>', views.edit_author, name='edit_author'),
    path('cat_books/<int:cat_id>', views.cat_books, name='cat_books')
]