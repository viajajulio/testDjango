from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'catalog/add_book.html', {'form': form})