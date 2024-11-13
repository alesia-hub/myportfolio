from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=250)
    # soring image of our project into specific folder:
    url = models.URLField(blank=True)

    def __str__(self):
        return str(self.title)
