from django.http import HttpResponseRedirect
from django.shortcuts import render

from book_app.forms import BookForm
from book_app.models import Book


# Create your views here.


def books(request):
    all_books = Book.objects.all()
    return render(request, "index.html", {"books": all_books})


def add_book(request):
    if request.method == "POST":
        form_data = BookForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            book = form_data.save()
            book.user = request.user
            book.cover_image = form_data.cleaned_data['cover_image']
            book.save()
            return HttpResponseRedirect("/books")

    return render(request, "add_book.html", context={"form": BookForm})


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "book_details.html", {"book": book})
