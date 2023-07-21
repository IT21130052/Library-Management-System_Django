from django.shortcuts import render, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'booklist/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        Book.objects.create(title=title, author=author, genre=genre, price=price, quantity=quantity)
        return redirect('book_list')
    return render(request, 'booklist/book_create.html')

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.genre = request.POST.get('genre')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.save()
        return redirect('book_list')
    return render(request, 'booklist/book_update.html', {'book': book})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')

def book_search(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query) | Book.objects.filter(genre__icontains=query) | Book.objects.filter(quantity__icontains=query)
    return render(request, 'booklist/book_search.html', {'books': books, 'query': query})

