from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from django.contrib import auth
from django.shortcuts import redirect
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
    return render(request, 'second_app/hs_app.html')

def registration(request):
    return render(request, 'second_app/sign_up.html')

def mission(request):
    return render(request, 'second_app/Our_Mission.html')

def signin(request):
    return render(request,'second_app/signin.html')

def checklist(request):
    return render(request,'staticfiles/Zawadi_checklist.docx')
