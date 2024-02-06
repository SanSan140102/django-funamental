from django.db import models

# Create your models here.


class Member(models.Model):
    nama           = models.CharField(max_length=100)
    alamat         = models.CharField(max_length=100)
    no_telphon     =models.CharField(max_length=100)
    jenis_kelamain =models.TextField()
    pekerjaan      =models.TextField()
    
    
    
    

