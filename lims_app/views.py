from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

# Create your views here.
from . models import *
def home(request):
    return render(request,"home.html", context={"current_tab": "home"})
def readers(request):
    return render(request,"readers.html", context={"current_tab": "readers"})
def browse_books (request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        book = Book.objects.get(id=book_id)
        if book.available:
            book.available = False
            book.save()
        return redirect('books')
    books = Book.objects.all()
    return render(request,"books.html", context={"current_tab": "books", "books": books})

def shopping(request):
    return HttpResponse("Welcome to shopping")
def save_student(request):
    student_name = request.POST['student_name']
    return render(request,"welcome.html",context={'student_name':student_name})
def readers_tab(request):
    if request.method=="GET":
        readers = reader.objects.all()
        return render(request,"readers.html",
                  context={"current_tab": "readers",
                                                  "readers": readers})
    else:
        query = request.POST['query']
        readers = reader.objects.raw("select * from lims_app_reader where reader_name like '%"+query+"%'")
        return render(request,"readers.html",
                  context={"current_tab": "readers",
                                                  "readers": readers, "query": query})
def save_reader(request):
    reader_item = reader(reference_id=request.POST["reader_ref_id"],
                         reader_name=request.POST['reader_name'],
                         reader_contact=request.POST['reader_contact'],
                         reader_address=request.POST["address"],
                         active=True
                         )
    reader_item.save()
    return redirect('/readers')
def save_books(request):
    book_item = Book(book_title = request.POST["book_title"],
                     book_author = request.POST["book_author"],
                     book_description = request.POST["book_description"],
                     available = True
                     )
    book_item.save()
    return redirect('/books')
def my_bag(request):
    return render(request, "my_bag.html", context={"current_tab": "bag"})


def add_to_bag(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = get_object_or_404(Book, id=book_id)


        bag = request.session.get("bag", [])
        bag.append({
            "id": book.id,
            "title": book.book_title,
            "author": book.book_author,
            "description": book.book_description,
        })
        request.session["bag"] = bag

        return redirect("/bag")
def remove_from_bag(request, book_id):
    # Retrieve the bag from the session
    bag = request.session.get("bag", [])

    # Filter out the book with the given ID
    bag = [book for book in bag if book["id"] != book_id]

    # Save the updated bag back to the session
    request.session["bag"] = bag

    return redirect("/bag")
