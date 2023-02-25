from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    @classmethod
    def get_default_collection(cls)-> "Collection":
        collection , _ = cls.objects.get_or_create(name="Defaut", slug="_defaut")
        return collection
