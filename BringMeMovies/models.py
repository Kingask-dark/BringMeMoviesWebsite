from django.db import models
from django.contrib.auth.models import User


class SearchedMovies(models.Model):
    id = models.AutoField(primary_key=True)
    Serchmovie = models.CharField(max_length=50)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self) :
        return self.Serchmovie



