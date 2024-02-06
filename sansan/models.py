from django.db import models

# Create your models here.

class barang(models.Model):
    nama_barang = models.CharField(max_length=100)
    size_barang = models.IntegerField()
    warna_barang =models.TextField()
    