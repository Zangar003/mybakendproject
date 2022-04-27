from django.core.mail import EmailMessage

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from startproject import settings
from .forms import BookCreate, AddPostForm, EmailForm
from django.http import HttpResponse


# Create your views her
from django.shortcuts import render, redirect
from .models import *
from .forms import BookCreate
from django.http import HttpResponse

#DataFlair
def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'book/upload_form.html', {'upload_form':upload})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form':book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')



def base(request):
    return render(request, 'book/base.html')


def addpage(request):
    title = "New form"
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Form_lab.objects.create(**form.cleaned_data)

                return redirect('index')
            except:
                form.add_error(None, 'Error')
    else:
        form = AddPostForm()
    return render(request, 'book/addpage.html', {'form':form, 'title':title})



from django.views.generic import ListView, DetailView

class ArticleListView(ListView):
    model = Posts
    template_name = "book/article_list.html"


class ArticleDetailView(DetailView):
    model = Posts
    template_name = "book/article_detail.html"

from django.core import mail
connection = mail.get_connection()

def sendMail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        if form.is_valid():

            message = form.cleaned_data['message']

            subject = "Sending an email with Django"
            gmail2 = request.POST['input']

            list = gmail2.split(',')
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,list)

            # set the variable initially created to True
            messageSent = True
    else:
        form = EmailForm()


    return render(request, 'gmail/index.html', {
        'form': form,

        'messageSent': messageSent,

    })

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

        else:
            return redirect('signup')

        messages.success(request, 'your account has been successfully created. ')
        return redirect('signin')
    return render(request, 'registration/signup.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            return render(request, 'book/library.html')
        else:
            messages.error(request, 'Bad Created')
            return redirect('signin')

    return render(request, 'registration/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"logged sussesfuly")
    return redirect('index')
