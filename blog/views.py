from django.shortcuts import render, redirect
from .models import post
from .forms import ContactForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    name = "Snooker"
    lastname = "dfdfdf"

    all_posts = post.objects.all()
    context = {
        'posts': all_posts,
    }

    return render(request, 'blog/home.html', context)

@login_required(login_url='sign_in')
def post_detail(request, post_id):
    single_post = post.objects.get(id=post_id)

    return render(request, 'blog/post_detail.html', {'post':single_post})

@login_required(login_url='sign_in')
def contact(request):

    # ถ้าเรา submit มันจะเข้าเงื่อนไข if แต่ถ้าเราไม่ submit คลิก form เฉยๆ มันจะเข้า else ( form เปล่า)
    
    form = ContactForm(request.POST)
    if form.is_valid():
        #Save to DB
        form.save()
        return redirect("/") #return to Home page
    else:
        form = ContactForm()

    # วิธีการเช็ค DEBUG GET/POST
    # if request.method == 'POST':
    #     pass
    # else:
    #     print("This is get")

    return render(request, 'blog/contact.html', {'form': form})


def register(request):
    regis = RegisterForm
    if request.method == 'POST':
        regis = RegisterForm(request.POST)
        if regis.is_valid():
            regis.save()
            return redirect("/")
    else:
        regis = RegisterForm()

    return render(request, 'blog/register.html', {'regis': regis})


def sign_in(request):
    if request.method == 'POST':
        username_form = request.POST["username"]
        password_form = request.POST["password"]
        user = authenticate(request, username=username_form, password=password_form)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Login Unsuccess")

    return render(request, 'blog/sign_in.html')


def sign_out(request):
    logout(request)
    return redirect("/")


