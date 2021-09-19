from django.contrib.auth import get_user_model
from django.db import models


class CookieStand(models.Model):

    hourly_sales = models.TextField()

    def __str__(self):
        return self.name


