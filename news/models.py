from django.db import models
from django.utils.text import slugify 
from django.utils import timezone
from django.contrib.auth.models import User


class Category (models.Model):
    category = models.CharField(max_length=100)
    def __str__(self) :
        return self.category



class News (models.Model):
     id= models.AutoField(primary_key=True)
     category  = models.ForeignKey(Category,on_delete=models.CASCADE)
     title     = models.CharField(max_length=100)
     deskripsi = models.TextField()
     image     = models.ImageField(upload_to='media/',null=True,blank=True)
     tanggal   = models.DateTimeField(default=timezone.now)
     slug      = models.SlugField(unique=True,blank=True,editable=False)
     total_views=models.PositiveIntegerField(default=0)
     def save(self, *args, **kwargs):
         if not self.slug or self.slug != slugify(self.title):
             self.slug=slugify(self.title)
         super().save(*args, **kwargs)
         
         
         
class Komentar(models.Model):
    posting = models.ForeignKey(News, on_delete=models.CASCADE, related_name='komentar')
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    teks = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Komentar oleh {self.penulis} pada {self.posting.judul}'
    
   
       
class ReplayKomentar(models.Model):
    komentar = models.ForeignKey(Komentar, on_delete=models.CASCADE, related_name='reply')
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    teks = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Komentar oleh {self.penulis} pada {self.posting.judul}'
    
    
class Like (models.Model):
     likes = models.ForeignKey(News, on_delete=models.CASCADE, related_name='like')
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # posting = models.ForeignKey(News, on_delete=models.CASCADE)
    # penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    # teks = models.TextField()
    # dibuat_pada = models.DateTimeField(auto_now_add=True)
    
    

    # def __str__(self):
    #     return f'Komentar oleh {self.penulis} pada {self.posting.judul}'


         

    

    
    

