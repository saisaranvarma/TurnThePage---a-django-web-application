from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Admin
from .forms import AuthorForm,BookForm

# def createbook(request):
#     books = Book.objects.all()
#     if request.method=='POST':
#
#         title=request.POST.get('title')
#         price=request.POST.get('price')
#
#         book=Book(title=title,price=price)
#         book.save()
#
#     return render(request,'book.html',{'books':books})

def detailsView(request,pk):
    book = Book.objects.get(id=pk)
    return render(request,'detailsview.html',{'book':book})

# def updateBook(request,pk):
#     book = Book.objects.get(id=pk)
#
#     if request.method == "POST":
#
#         title = request.POST.get("title")
#         price = request.POST.get("price")
#
#         book.title=title
#         book.price=price
#
#         book.save()
#         return redirect('/')
#
#     return render(request,'updateview.html',{'book':book})


def deleteView(request,pk):
    book = Book.objects.get(id=pk)

    if request.method == "POST":
        book.delete()

        return redirect('list')

    return render(request,'deleteview.html',{'book':book})


def createbook(request):
    books=Book.objects.all()

    if request.method == 'POST':
        form=BookForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
    else:
        form=BookForm()

    return render(request,'book.html',{'form':form,'books':books})

def Create_Author(request):
    if request.method=='POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('list')
    else:
        form=AuthorForm()

    return render(request,'author.html',{'form':form})


def updateBook(request,pk):
    book=Book.objects.get(id=pk)

    if request.method=='POST':
        form = BookForm(request.POST,request.FILES,instance=book)

        if form.is_valid():
            form.save()

            return redirect('list')

    else:
        form=BookForm(instance=book)

    return render(request,'updateview.html',{'form':form})


def index(request):
    return render(request,'base.html')


def ListBook(request):
    books = Book.objects.all()

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request,'listbook.html',{'books':books,'page':page})

def search_Book(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))

    else:
        books=[]
    context={'books':books,'query':query}
    return render(request,'search.html',context)


def Register_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists!')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists!")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()

            return redirect('login')

        else:
            messages.info(request,'passwords dont match!')
            return redirect('register')

    return render(request,'register.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('userlist')
        else:
            messages.info(request,'please provide correct info!')
            return redirect('login')



    return render(request,'login.html')

def logOut(request):
    auth.logout(request)
    return redirect('login')


def admin_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Check if the admin details match any record in the database
        try:
            admin = Admin.objects.get(name=name, password=password)
            # If the admin exists, redirect to the 'list' page
            return redirect('list')
        except Admin.DoesNotExist:
            # If the admin does not exist, show an error message
            messages.error(request, 'Invalid name or password')
            return redirect('adminlogin')

    return render(request, 'adminlogin.html')