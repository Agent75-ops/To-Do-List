from ast import Not
from asyncio.windows_events import NULL
from sqlite3 import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .models import Users

def login_user(request) :
    if request.method == "POST" :
        email = request.POST['email']
        passs= request.POST['password']
        auth = authenticate(username=email, password=passs)
        if auth is not None : 
            login(request,request.user)
            return HttpResponseRedirect(reverse("form:main"))
        else : 
            return render(request, "form/login.html",{
                "errorr": True,
                "error" : "wrong info"
            })
    else: 
        return render(request, "form/login.html")

def register_user(request):
    if request.method == "POST" :
        email = request.POST['email']
        username= request.POST['name']
        passw = request.POST['pass']
        confpass= request.POST['confpass']
        
        if (not email and not username and not passw) or (not email and not username) or not email or not username or not passw: 
            return render(request, 'form/register.html',{
                'emailerror' : 'email required !' if not email else '',
                'uerror' : 'username required !' if not username else '',
                'perror' : 'password required !' if not passw else ' '

            })
        # if not email and not username: 
        #     return render(request, "form/register.html", {
        #     'emailerror' : "email required !",
        #     "uerror" : "username required !"
        # })
        # if not username: 
        #     return render(request, "form/register.html", {
        #         'uerror' : "username required !"
        #     })
        # if not email: 
        #     return render(request, "form/register.html", {
        #         'emailerror' : "email required !"
        #     })
        
        
        if passw != confpass : 
            return render(request, "form/register.html", {
                'error' : "passwords don't match !"
            })

        auth = authenticate(username=email, passwrod=passw)
        if auth is not None :
            return render(request, "form/register.html", {
                'error': "email already used"
            })
        else :
            try : 
                user = Users.objects.create_user(email = email, username = username, password=passw)
            except :
                return render(request, "form/register.html",{
                    'error' : "email already exists "
                }) 
            login(request, user)
            return HttpResponseRedirect(reverse("form:main"))
    else : 
        return render(request, "form/register.html")


def mainf(request):
    return render(request, "form/main.html")
