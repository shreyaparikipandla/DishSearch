from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'dishsearchapp_dish'

