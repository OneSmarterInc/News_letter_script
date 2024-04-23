from django.db import models

class Credentials(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=255)
    Date = models.DateTimeField(auto_now_add=True)
    image_link = models.CharField(max_length=255)
    
