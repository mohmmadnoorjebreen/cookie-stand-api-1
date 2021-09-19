from django.contrib.auth import get_user_model
from django.db import models


class CookieStand(models.Model):

    hourly_sales = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name


