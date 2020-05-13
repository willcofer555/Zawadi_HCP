from django.shortcuts import render, redirect
from django.http import HttpResponse
from pyrebase import pyrebase
from django.contrib import auth
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings




config = {

"apiKey": "AIzaSyB5LoorIbepF-rlYWlFABTgTRT2jZtCOnI",
"authDomain": "login-info-zhg.firebaseapp.com",
"databaseURL": "https://login-info-zhg.firebaseio.com",
"projectId": "login-info-zhg",
"storageBucket": "login-info-zhg.appspot.com",
"messagingSenderId": "890643987237",
"appId": "1:890643987237:web:49a3775fd03661668438cc"
}
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()

session_id = []

database = firebase.database()

def signIn(request):

    return render(request, "second_app/signIn.html")


def index(request):
    my_dictionary = {'insert_me':" I am from another galaxy"}
    return render(request,'second_app/index.html',context=my_dictionary)


def contact(request):
    return render(request, 'second_app/Contactus.html')

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid credentials"
        return render(request,'second_app/signin.html',{"messg":message})
    print(user['idToken'])
    request.session['uid']=str(session_id)
    return render(request, 'second_app/welcome.html',{"e":email})

def logout(request):
    auth.logout(request)
    return render(request,'second_app/signIn.html')

def FAQ(request):
    return render(request, 'second_app/FAQ_page.html')

def signup():
    return render(request, 'second_app/sign_up.html')

def postsignup(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
    except:
        message="unable to create account, please try again "
        return render(request,signIn.html,{"messg":message})
        uid = user['localId']

    data={"name":name,"status":"1"}

    database.child("users").child(uid).child("details").set(data)
    return render(request,"signin.html")

def resources(request):
    return render(request, 'second_app/Resources.html')

def apply(request):
    return render(request, 'second_app/placeholder_app2.html')

def registration(request):
    return render(request, 'second_app/sign_up.html')

def mission(request):
    return render(request, 'second_app/Our_Mission.html')

def signin(request):
    return render(request,'second_app/signin.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('second_app:login_url')
    else:
        form = UserCreationForm()

    return render(request,'registration/register.html',{'form':form})

def home(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'registration/signup.html')

def indexView(request):
    return render(request,'placeholder.html')


class RequireLoginMiddleware(object):
    def __init__(self):
        self.required = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS)
        self.exceptions = tuple(re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # No need to process URLs if user already logged in
        if request.user.is_authenticated():
            return None

        # An exception match should immediately return None
        for url in self.exceptions:
            if url.match(request.path):
                return None

        # Requests matching a restricted URL pattern are returned
        # wrapped with the login_required decorator
        for url in self.required:
            if url.match(request.path):
                return login_required(view_func)(request, *view_args, **view_kwargs)

        # Explicitly return None for all non-matching requests
        return None

"""
def redirect_view(request):
    response = redirect('/registration/login/')
    return response


def login_url(request):
    return render(request,)
"""
