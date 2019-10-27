from django.db import models
from django.urls import reverse
# Create your models here.
class employees(models.Model):
    firstname = models.CharField(max_length = 14)
    lastname = models.CharField(max_length = 14)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse("Detail", kwargs={"id": self.id})
    