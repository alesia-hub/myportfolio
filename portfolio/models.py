from django.db import models
from django.urls import reverse
from django.db.models.manager import Manager

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # storing image of our project into specific folder:
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    objects: Manager['Project']  # type hint for static checkers

    # def get_internal_url(self):
    #     return reverse('blog/', kwargs={'project_id': self.id})

    def __str__(self):
        return str(self.title)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=250)
    # soring image of our project into specific folder:
    url = models.URLField(blank=True)

    objects: Manager['Blog']  # type hint for static checkers

    def __str__(self):
        return str(self.title)
