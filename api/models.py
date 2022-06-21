from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta : 
        ordering = ['-updated_at']    
