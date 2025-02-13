from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # storing image of our project into specific folder:
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    # def get_internal_url(self):
    #     return reverse('blog/', kwargs={'project_id': self.id})



    def __str__(self):
        return str(self.title)
