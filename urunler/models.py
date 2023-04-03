from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Kategori(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Urun(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True, blank=True)
    isim = models.CharField(max_length=200, verbose_name="Ürün ismi")
    resim = models.FileField(upload_to="urunResmi", null=True, blank=True, verbose_name="Ürün resmi")
    fiyat = models.IntegerField(null=True)

    def __str__(self):
        return self.isim

class Sepet(models.Model):
    secen = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    urunler = models.ManyToManyField(Urun, blank=True)

    def __str__(self):
        return self.secen.username