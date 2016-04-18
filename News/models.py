from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        if self.is_published:
            return self.title + '    (*)'
        else:
            return self.title

    def sort_info(self):
        return self.text[:250] + '...'
