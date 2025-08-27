from django.db import models

class post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    featured_pic = models.ImageField(upload_to='featured_pics/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    subject = models.CharField(max_length=50)
    email = models.EmailField()
    sender = models.CharField(max_length=50)
    detail = models.TextField()

