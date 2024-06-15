from django.shortcuts import render, get_object_or_404, redirect

from books.models import Book, Category, Author


# Create your views here.


def base(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    ctx  = {
        'books':books,
        'categories' : categories,
        'authors': authors
    }
    return render(request, 'books/base.html', context=ctx)


def book_info(request, book_id):
    book = get_object_or_404(Book, pk=book_id)


    return render(request, 'books/book_info.html', context={'book':book})



def add_book(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    ctx = {
        'categories':categories,
        'authors':authors
    }
    if request.method == 'POST':
        book = Book()
        book.name = request.POST.get('book_name')
        book.description = request.POST.get('book_description')
        book.author = Author.objects.get(name=request.POST.get('book_author'))
        if book.name != '' and book.name != None and book.author != None and book.author != '':
            book.save()
    return render(request,'books/add_book.html', context=ctx)


def add_cat(request):
    cat = Category()
    if request.method == 'POST':
        cat.name = request.POST.get('cat_name')
        if cat.name != '' and cat.name != None:
            cat.save()

    return redirect('base')



def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('base')


def delete_cat(request, cat_id):
    category = Category.objects.get(id=cat_id)
    category.delete()
    return redirect('base')


def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    return redirect('base')


def add_author(request):
    author = Author()
    if request.method == "POST":
        author.name = request.POST['author_name']
        author.bio = request.POST['author_bio']
        if author.name != '' and author.name != None:
            author.save()
    return render(request, 'books/add_author.html')


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.name = request.POST['new_book_name']
        if book.name != '' and book.name != None:
            book.save()
    return render(request, 'books/edit_book.html')


def edit_cat(request, cat_id):
    category = Category.objects.get(id=cat_id)
    if request.method == 'POST':
        category.name = request.POST['new_cat_name']
        if category.name != '' and category.name != None:
            category.save()
    return render(request, 'books/edit_cat.html')


def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        author.name = request.POST['new_author_name']
        if author.name != '' and author.name != None:
            author.save()
    return render(request, 'books/edit_author.html')


def cat_books(request, cat_id):
    category = Category.objects.get(id=cat_id)
    books = category.books.all()
    print(books)
    return render(request, 'books/cat_books.html', context={'books':books})


