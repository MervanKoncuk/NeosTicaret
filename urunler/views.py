from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    kategoriler = Kategori.objects.all()
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        urunler = Urun.objects.filter(
            Q(isim__icontains=search_query) |
            Q(kategori__name__icontains = search_query) |
            Q(fiyat__icontains = search_query) |
            Q(owner__username__icontains = search_query)
            )
    

    context = {
        'urunler':urunler,
        'kategori':kategoriler,
        'search_query':search_query
    }

    
    return render(request, "index.html", context)

def filter(request, id):
    kategoriler = Kategori.objects.all()
    urun = Urun.objects.filter(kategori = id)
    kategoriler = Kategori.objects.all()
    context = {
        'urun':urun,
        'kategori':kategoriler
    }
    return render(request, "kategoriler.html", context)

def create(request):
    kategoriler = Kategori.objects.all()
    form = UrunForm()
    if request.method == "POST":
        form = UrunForm(request.POST, request.FILES)
        if form.is_valid():
            urun = form.save(commit=False)
            urun.owner = request.user
            urun.save()
            messages.success(request, "Ürün başarıyla eklendi.")
            return redirect('index')
    context = {
        'form':form,

        'kategori':kategoriler
    }
    return render(request, "create.html", context)

def sepet(request):
    kategoriler = Kategori.objects.all()
    sepet = Sepet.objects.get(secen = request.user)
    eklenen = sepet.urunler.all()
    print(eklenen)
    context = {
        'sepet':sepet,
        'eklenen':eklenen,
        'kategori':kategoriler
    }
    return render(request, "sepet.html", context)