from django.db import models

# Create your models here.

class NssUpload(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   
