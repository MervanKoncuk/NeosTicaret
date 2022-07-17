from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def userRegister(request):
    form = UserCreate()
    if request.method == "POST":
        form = UserCreate(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            subject = 'NeosTicaret'
            message = 'NeosTicaret sayfasına hoş geldiniz!'
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            messages.success(request, "Kullanıcı başarıyla oluşturuldu.")
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, "register.html", context)

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Başarıyla giriş yaptınız.")
            return redirect('index')
        else:
            messages.error(request, "Kullanıcı adı veya şifre hatalı.")
    return render(request, "login.html")

def userLogout(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız.")
    return redirect('index')

def mail(request):
    users = User.objects.all()
    baslik = request.POST.get('subject')
    print(baslik)
    mesaj = request.POST.get('message')
    subject = baslik
    message = mesaj
    for i in users:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [i.email],
            fail_silently=False,
        )

    return render(request, "mail.html")